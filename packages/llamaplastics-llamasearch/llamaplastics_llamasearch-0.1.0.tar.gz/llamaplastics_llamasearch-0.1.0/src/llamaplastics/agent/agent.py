import os
import logging
import time
import numpy as np
import jax
import jax.numpy as jnp
from typing import Dict, List, Any, Callable, Optional, Tuple
from datetime import datetime
import pickle

from .planner import ExperimentPlanner
from .executor import ExperimentExecutor
from .analyzer import ResultsAnalyzer

"""
Agent module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


class DiscoveryAgent:
    """
    Autonomous agent for materials discovery.
    Orchestrates the planning, execution, and analysis of experiments.
    """

    def __init__(
        self,
        config: Dict[str, Any],
        llm_embedder: Any,
        predictor_head_apply: Callable,
        experiment_runner: Callable,
        train_head_fn: Callable,
        data_store: Any,
        save_dir: str = "agent_results",
    ):
        """
        Initialize the discovery agent.

        Args:
            config: Configuration dictionary
            llm_embedder: LLM embedder instance
            predictor_head_apply: JAX function to apply the prediction head
            experiment_runner: Function to run experiments (real or simulated)
            train_head_fn: Function to train the prediction head
            data_store: Data store instance
            save_dir: Directory to save results
        """
        self.config = config
        self.llm_embedder = llm_embedder
        self.predictor_head_apply = predictor_head_apply
        self.experiment_runner = experiment_runner
        self.train_head_fn = train_head_fn
        self.data_store = data_store

        # Initialize RNG
        self.rng_key = jax.random.PRNGKey(config["seed"])

        # Initialize predictor params (will be set after training)
        self.predictor_params = None

        # Create save directory
        self.save_dir = os.path.join(
            save_dir, f"agent_run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        os.makedirs(self.save_dir, exist_ok=True)

        # Initialize agent components
        self.planner = ExperimentPlanner(config, self.rng_key)
        self.executor = ExperimentExecutor(config, experiment_runner)
        self.analyzer = ResultsAnalyzer(config)

        # Set up logging
        self.setup_logging()

        # Track agent state
        self.state = {
            "iteration": 0,
            "total_experiments": 0,
            "discovery_phase": "initialization",
            "best_compositions": {},
            "exploration_rate": 1.0,
            "history": [],
        }

        logger.info("Discovery Agent initialized")

    def setup_logging(self) -> None:
        """Set up logging for the agent."""
        log_file = os.path.join(self.save_dir, "agent.log")
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        logger.setLevel(logging.INFO)

    def initialize(self) -> None:
        """Initialize the agent with bootstrap data and initial model."""
        logger.info("Initializing agent with bootstrap data...")

        # Check if we need to collect initial data
        if len(self.data_store) < self.config["active_learning"]["initial_dataset_size"]:
            logger.info(
                f"Collecting initial data (need {self.config['active_learning']['initial_dataset_size']} samples)..."
            )

            # Generate initial compositions
            n_needed = self.config["active_learning"]["initial_dataset_size"] - len(self.data_store)
            self.rng_key, subkey = jax.random.split(self.rng_key)
            initial_compositions = self.planner.generate_diverse_candidates(n_needed, subkey)

            # Run experiments
            for comp in initial_compositions:
                result = self.executor.run_experiment(comp)
                self.data_store.add_data(comp, result)
                self.state["total_experiments"] += 1

            logger.info(f"Collected {n_needed} initial samples")

        # Train initial model
        logger.info("Training initial prediction model...")
        self._train_model()

        # Update state
        self.state["discovery_phase"] = "exploration"
        self.state["iteration"] = 1

        # Save initial state
        self._save_state()

        logger.info("Agent initialization complete")

    def _train_model(self) -> None:
        """Train the prediction model on current data."""
        # Format compositions into text prompts
        compositions = self.data_store.get_compositions()
        template = self.config["data"]["text_prompt_template"]
        prompts = [self._format_composition(comp) for comp in compositions]

        # Get embeddings
        embeddings = self.llm_embedder.get_embeddings(
            prompts, batch_size=self.config["llm"]["batch_size"], use_cache=True
        ).numpy()

        # Get properties
        properties = self.data_store.get_properties()

        # Train head
        self.rng_key, subkey = jax.random.split(self.rng_key)
        self.predictor_params, train_metrics = self.train_head_fn(
            embeddings, properties, rng_key=subkey
        )

        logger.info(f"Model trained. Final metrics: {train_metrics[-1]}")

        # Save model
        with open(
            os.path.join(self.save_dir, f"model_iter_{self.state['iteration']}.pkl"), "wb"
        ) as f:
            pickle.dump(
                {
                    "params": self.predictor_params,
                    "metrics": train_metrics,
                    "iteration": self.state["iteration"],
                },
                f,
            )

    def _format_composition(self, composition: Dict[str, float]) -> str:
        """Format a composition into a text prompt."""
        template = self.config["data"]["text_prompt_template"]

        # Add processing params (default values)
        processing = {"processing_temp": 60, "drying_time": 24}

        # Format using string formatting
        try:
            format_dict = {**composition, **processing}
            return template.format(**format_dict)
        except KeyError as e:
            logger.warning(f"Missing key {e} in composition/processing data for template.")
            # Fallback
            return f"Material Composition: {', '.join([f'{k} {v:.2f}' for k, v in composition.items()])}. Processing: temp 60°C, time 24h."

    def _predict_properties(
        self, compositions: List[Dict[str, float]]
    ) -> Tuple[np.ndarray, np.ndarray]:
        """
        Predict properties for a list of compositions.

        Args:
            compositions: List of composition dictionaries

        Returns:
            Tuple of (means, variances) arrays
        """
        # Format compositions
        prompts = [self._format_composition(comp) for comp in compositions]

        # Get embeddings
        embeddings = self.llm_embedder.get_embeddings(
            prompts, batch_size=self.config["llm"]["batch_size"]
        ).numpy()
        embeddings_jnp = jnp.array(embeddings)

        # Predict with uncertainty
        if self.config["predictor_head"]["use_uncertainty"]:
            # MC Dropout for uncertainty
            predictions = []
            log_vars = []

            for _ in range(self.config["predictor_head"]["mc_dropout_samples"]):
                self.rng_key, dropout_key = jax.random.split(self.rng_key)
                mc_preds, mc_log_vars = self.predictor_head_apply(
                    {"params": self.predictor_params},
                    embeddings_jnp,
                    training=True,
                    rngs={"dropout": dropout_key},
                )
                predictions.append(mc_preds)
                log_vars.append(mc_log_vars)

            # Calculate mean and variance
            pred_means = jnp.mean(jnp.stack(predictions), axis=0)
            pred_epistemic_vars = jnp.var(jnp.stack(predictions), axis=0)
            pred_aleatoric_vars = jnp.exp(jnp.mean(jnp.stack(log_vars), axis=0))
            pred_total_vars = pred_epistemic_vars + pred_aleatoric_vars

            return np.array(pred_means), np.array(pred_total_vars)
        else:
            # Deterministic prediction
            predictions = self.predictor_head_apply(
                {"params": self.predictor_params}, embeddings_jnp, training=False
            )

            return np.array(predictions), np.zeros_like(np.array(predictions))

    def _save_state(self) -> None:
        """Save the current agent state."""
        state_file = os.path.join(self.save_dir, f"agent_state_iter_{self.state['iteration']}.pkl")
        with open(state_file, "wb") as f:
            pickle.dump(self.state, f)

        logger.info(f"Agent state saved to {state_file}")

    def run_iteration(self) -> Dict[str, Any]:
        """
        Run a single iteration of the agent's discovery cycle.

        Returns:
            Dictionary of iteration results
        """
        iteration_start = time.time()
        logger.info(f"\n--- Agent Iteration {self.state['iteration']} ---")

        # 1. Plan experiments based on current state
        logger.info("Planning experiments...")

        # Adjust exploration rate based on iteration
        max_iterations = self.config.get("agent", {}).get("max_iterations", 50)
        self.state["exploration_rate"] = max(0.1, 1.0 - (self.state["iteration"] / max_iterations))

        # Generate candidates based on current phase
        self.rng_key, subkey = jax.random.split(self.rng_key)
        if self.state["discovery_phase"] == "exploration":
            # Exploration phase: focus on uncertainty and diversity
            candidates = self.planner.generate_exploration_candidates(
                n_candidates=self.config["active_learning"]["candidate_pool_size"],
                exploration_rate=self.state["exploration_rate"],
                rng_key=subkey,
            )
        elif self.state["discovery_phase"] == "exploitation":
            # Exploitation phase: focus on promising regions
            candidates = self.planner.generate_exploitation_candidates(
                n_candidates=self.config["active_learning"]["candidate_pool_size"],
                best_compositions=self.state["best_compositions"],
                rng_key=subkey,
            )
        elif self.state["discovery_phase"] == "optimization":
            # Optimization phase: refine best candidates
            candidates = self.planner.generate_optimization_candidates(
                n_candidates=self.config["active_learning"]["candidate_pool_size"],
                best_compositions=self.state["best_compositions"],
                rng_key=subkey,
            )
        else:
            # Default to balanced approach
            candidates = self.planner.generate_balanced_candidates(
                n_candidates=self.config["active_learning"]["candidate_pool_size"],
                exploration_rate=self.state["exploration_rate"],
                rng_key=subkey,
            )

        # 2. Predict properties and select experiments
        logger.info("Predicting properties and selecting experiments...")
        pred_means, pred_vars = self._predict_properties(candidates)

        # Select experiments based on acquisition function
        self.rng_key, acq_key = jax.random.split(self.rng_key)
        selected_indices, acquisition_scores = self.planner.select_experiments(
            pred_means,
            pred_vars,
            n_experiments=self.config["active_learning"]["num_experiments_per_loop"],
            acquisition_function=self.config["active_learning"]["acquisition_function"],
            rng_key=acq_key,
        )

        selected_candidates = [candidates[i] for i in selected_indices]
        selected_scores = [acquisition_scores[i] for i in selected_indices]

        # 3. Execute experiments
        logger.info("Executing experiments...")
        results = []
        for comp, score in zip(selected_candidates, selected_scores):
            result = self.executor.run_experiment(comp)
            self.data_store.add_data(comp, result)
            results.append(result)
            self.state["total_experiments"] += 1

            # Log experiment
            prop_str = ", ".join([f"{k}: {v:.4f}" for k, v in result.items()])
            logger.info(f"Experiment result: {prop_str} (acquisition score: {score:.4f})")

        # 4. Analyze results
        logger.info("Analyzing results...")
        analysis = self.analyzer.analyze_results(
            candidates=selected_candidates,
            results=results,
            all_data=self.data_store,
            iteration=self.state["iteration"],
        )

        # Update best compositions
        for prop, comp in analysis["best_compositions"].items():
            if prop not in self.state["best_compositions"] or analysis["best_values"][
                prop
            ] > self.state["best_values"].get(prop, float("-inf")):
                self.state["best_compositions"][prop] = comp
                self.state["best_values"] = analysis["best_values"]

        # 5. Retrain model with new data
        logger.info("Retraining model with new data...")
        self._train_model()

        # 6. Update agent state and strategy
        self._update_strategy(analysis)

        # Record iteration results
        iteration_results = {
            "iteration": self.state["iteration"],
            "time_taken": time.time() - iteration_start,
            "experiments": list(zip(selected_candidates, results)),
            "acquisition_scores": selected_scores,
            "analysis": analysis,
            "phase": self.state["discovery_phase"],
            "exploration_rate": self.state["exploration_rate"],
        }

        self.state["history"].append(iteration_results)

        # Save state
        self._save_state()

        # Increment iteration
        self.state["iteration"] += 1

        logger.info(
            f"Iteration {self.state['iteration']-1} completed in {iteration_results['time_taken']:.2f} seconds"
        )

        return iteration_results

    def _update_strategy(self, analysis: Dict[str, Any]) -> None:
        """
        Update the agent's strategy based on analysis.

        Args:
            analysis: Analysis results from the analyzer
        """
        # Determine phase based on progress and results
        current_phase = self.state["discovery_phase"]
        iteration = self.state["iteration"]

        # Simple state machine for phase transitions
        if current_phase == "exploration":
            if analysis["convergence_score"] > 0.7 or iteration > 10:
                self.state["discovery_phase"] = "exploitation"
                logger.info("Transitioning from exploration to exploitation phase")

        elif current_phase == "exploitation":
            if analysis["novelty_score"] < 0.3 or iteration > 20:
                self.state["discovery_phase"] = "optimization"
                logger.info("Transitioning from exploitation to optimization phase")

        elif current_phase == "optimization":
            if analysis["optimization_score"] > 0.9 or iteration > 30:
                # Could transition to a new phase or stay in optimization
                pass

    def run(self, n_iterations: int) -> Dict[str, Any]:
        """
        Run the agent for a specified number of iterations.

        Args:
            n_iterations: Number of iterations to run

        Returns:
            Dictionary of final results
        """
        logger.info(f"Starting agent run for {n_iterations} iterations")

        # Initialize if needed
        if self.predictor_params is None:
            self.initialize()

        # Run iterations
        for _ in range(n_iterations):
            self.run_iteration()

            # Optional: early stopping based on convergence
            if self.state.get("early_stop", False):
                logger.info("Early stopping triggered")
                break

        # Final analysis
        final_analysis = self.analyzer.generate_final_report(
            data_store=self.data_store, state=self.state
        )

        # Save final results
        final_results = {
            "state": self.state,
            "final_analysis": final_analysis,
            "best_compositions": self.state["best_compositions"],
            "best_values": self.state.get("best_values", {}),
        }

        with open(os.path.join(self.save_dir, "final_results.pkl"), "wb") as f:
            pickle.dump(final_results, f)

        logger.info("Agent run completed")

        return final_results
