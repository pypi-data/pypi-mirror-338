import numpy as np
import logging
from typing import Dict, List, Any, Optional
import matplotlib.pyplot as plt
import os
from datetime import datetime

"""
Analyzer module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


class ResultsAnalyzer:
    """
    Analyzes experimental results and provides insights to guide the agent.
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the results analyzer.

        Args:
            config: Configuration dictionary
        """
        self.config = config
        self.property_labels = config["data"]["property_labels"]

        # Initialize metrics
        self.metrics_history = {
            "convergence_score": [],
            "novelty_score": [],
            "optimization_score": [],
        }

        logger.info("Results Analyzer initialized")

    def analyze_results(
        self,
        candidates: List[Dict[str, float]],
        results: List[Dict[str, float]],
        all_data: Any,
        iteration: int,
    ) -> Dict[str, Any]:
        """
        Analyze the results of the latest experiments.

        Args:
            candidates: List of tested compositions
            results: List of experimental results
            all_data: Data store containing all historical data
            iteration: Current iteration number

        Returns:
            Dictionary of analysis results
        """
        logger.info(f"Analyzing results from iteration {iteration}")

        # Convert results to numpy array
        results_array = np.array(
            [[r.get(prop, 0.0) for prop in self.property_labels] for r in results]
        )

        # Get all historical data
        all_properties = all_data.get_properties()

        # Find best compositions and values for each property
        best_compositions = {}
        best_values = {}

        for i, prop in enumerate(self.property_labels):
            # Find best in current batch
            if results_array.shape[0] > 0:
                batch_best_idx = np.nanargmax(results_array[:, i])
                batch_best_value = results_array[batch_best_idx, i]
                batch_best_comp = candidates[batch_best_idx]
            else:
                batch_best_value = float("-inf")
                batch_best_comp = None

            # Find best in all data
            all_values = all_properties[:, i]
            all_best_idx = np.nanargmax(all_values)
            all_best_value = all_values[all_best_idx]
            all_best_comp = all_data.get_compositions()[all_best_idx]

            # Use the better of the two
            if batch_best_value > all_best_value:
                best_compositions[prop] = batch_best_comp
                best_values[prop] = float(batch_best_value)
            else:
                best_compositions[prop] = all_best_comp
                best_values[prop] = float(all_best_value)

        # Calculate improvement over previous best
        if iteration > 1 and hasattr(self, "previous_best_values"):
            improvements = {}
            for prop in self.property_labels:
                prev_best = self.previous_best_values.get(prop, 0.0)
                current_best = best_values[prop]
                rel_improvement = (
                    (current_best - prev_best) / (abs(prev_best) + 1e-10) if prev_best != 0 else 0
                )
                improvements[prop] = rel_improvement
        else:
            improvements = {prop: 0.0 for prop in self.property_labels}

        # Store current best for next iteration
        self.previous_best_values = best_values.copy()

        # Calculate convergence score (how much improvement is slowing down)
        if len(self.metrics_history["convergence_score"]) > 0:
            prev_improvements = self.metrics_history.get("improvements", [])
            if prev_improvements:
                avg_prev_improvement = np.mean(
                    [imp for imp_dict in prev_improvements for imp in imp_dict.values()]
                )
                avg_current_improvement = np.mean(list(improvements.values()))
                convergence_score = 1.0 - min(
                    1.0, max(0.0, avg_current_improvement / (avg_prev_improvement + 1e-10))
                )
            else:
                convergence_score = 0.0
        else:
            convergence_score = 0.0

        # Calculate novelty score (how different new compositions are from previous ones)
        all_comps = all_data.get_compositions()
        if len(all_comps) > len(candidates):
            prev_comps = all_comps[: -len(candidates)]

            # Convert to arrays for distance calculation
            prev_comp_arrays = []
            for comp in prev_comps:
                comp_array = np.array(
                    [comp.get(k, 0.0) for k in self.config["data"]["composition_keys"]]
                )
                prev_comp_arrays.append(comp_array)

            candidate_arrays = []
            for comp in candidates:
                comp_array = np.array(
                    [comp.get(k, 0.0) for k in self.config["data"]["composition_keys"]]
                )
                candidate_arrays.append(comp_array)

            prev_comp_matrix = np.vstack(prev_comp_arrays) if prev_comp_arrays else np.array([])
            candidate_matrix = np.vstack(candidate_arrays)

            # Calculate minimum distance from each candidate to previous compositions
            if len(prev_comp_matrix) > 0:
                min_distances = []
                for i in range(len(candidate_matrix)):
                    dists = np.linalg.norm(prev_comp_matrix - candidate_matrix[i], axis=1)
                    min_distances.append(np.min(dists))

                avg_min_distance = np.mean(min_distances)
                # Normalize to [0, 1] with a reasonable scale
                novelty_score = min(1.0, avg_min_distance / 0.5)
            else:
                novelty_score = 1.0
        else:
            novelty_score = 1.0

        # Calculate optimization score (how close we are to theoretical optimum)
        # This is a placeholder - in a real system you'd have a better estimate
        best_known_values = {
            "Tvis": 0.95,  # Example theoretical maximum
            "RR": 0.95,
            "Strength_MPa": 80.0,
            "Strain_percent": 40.0,
            "Modulus_GPa": 5.0,
        }

        optimization_ratios = []
        for prop in self.property_labels:
            if prop in best_known_values and best_known_values[prop] > 0:
                ratio = best_values.get(prop, 0.0) / best_known_values[prop]
                optimization_ratios.append(min(1.0, ratio))

        optimization_score = np.mean(optimization_ratios) if optimization_ratios else 0.5

        # Update metrics history
        self.metrics_history["convergence_score"].append(convergence_score)
        self.metrics_history["novelty_score"].append(novelty_score)
        self.metrics_history["optimization_score"].append(optimization_score)

        if not hasattr(self, "metrics_history_improvements"):
            self.metrics_history_improvements = []
        self.metrics_history_improvements.append(improvements)

        # Generate analysis
        analysis = {
            "best_compositions": best_compositions,
            "best_values": best_values,
            "improvements": improvements,
            "convergence_score": convergence_score,
            "novelty_score": novelty_score,
            "optimization_score": optimization_score,
            "metrics_history": self.metrics_history,
        }

        logger.info(
            f"Analysis complete. Convergence: {convergence_score:.2f}, Novelty: {novelty_score:.2f}, Optimization: {optimization_score:.2f}"
        )

        return analysis

    def generate_final_report(self, data_store: Any, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a comprehensive final report.

        Args:
            data_store: Data store containing all experimental data
            state: Current agent state

        Returns:
            Dictionary containing the final report
        """
        logger.info("Generating final report")

        # Extract key information
        total_experiments = state["total_experiments"]
        best_compositions = state["best_compositions"]
        best_values = state.get("best_values", {})

        # Calculate improvement over initial values
        initial_properties = data_store.get_properties()[
            : state["active_learning"]["initial_dataset_size"]
        ]
        if len(initial_properties) > 0:
            initial_best = {}
            for i, prop in enumerate(self.property_labels):
                initial_best[prop] = float(np.nanmax(initial_properties[:, i]))

            total_improvements = {}
            for prop in self.property_labels:
                initial = initial_best.get(prop, 0.0)
                final = best_values.get(prop, 0.0)
                rel_improvement = (final - initial) / (abs(initial) + 1e-10) if initial != 0 else 0
                total_improvements[prop] = rel_improvement
        else:
            total_improvements = {prop: 0.0 for prop in self.property_labels}

        # Generate report
        report = {
            "total_experiments": total_experiments,
            "best_compositions": best_compositions,
            "best_values": best_values,
            "total_improvements": total_improvements,
            "metrics_history": self.metrics_history,
            "final_convergence": (
                self.metrics_history["convergence_score"][-1]
                if self.metrics_history["convergence_score"]
                else 0
            ),
            "final_optimization": (
                self.metrics_history["optimization_score"][-1]
                if self.metrics_history["optimization_score"]
                else 0
            ),
        }

        # Log summary
        logger.info(f"Final report generated. Total experiments: {total_experiments}")
        for prop, value in best_values.items():
            logger.info(
                f"Best {prop}: {value:.4f} (improvement: {total_improvements.get(prop, 0.0):.2%})"
            )

        return report
