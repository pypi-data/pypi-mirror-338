import jax
import jax.numpy as jnp
import numpy as np
from typing import Dict, List, Tuple, Any, Callable, Optional
import logging
from functools import partial

from active_learning.acquisition import get_acquisition_function

"""
Planner module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


class ExperimentPlanner:
    """
    Plans experiments by generating candidates and selecting the most informative ones.
    """

    def __init__(self, config: Dict[str, Any], rng_key: jax.random.PRNGKey):
        """
        Initialize the experiment planner.

        Args:
            config: Configuration dictionary
            rng_key: JAX random key
        """
        self.config = config
        self.rng_key = rng_key
        self.composition_keys = config["data"]["composition_keys"]

        logger.info("Experiment Planner initialized")

    def generate_diverse_candidates(
        self, n_candidates: int, rng_key: Optional[jax.random.PRNGKey] = None
    ) -> List[Dict[str, float]]:
        """
        Generate diverse candidates using space-filling designs.

        Args:
            n_candidates: Number of candidates to generate
            rng_key: JAX random key

        Returns:
            List of composition dictionaries
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        # Generate using Latin Hypercube Sampling (approximate)
        n_components = len(self.composition_keys)

        # Generate uniform samples in [0, 1] for each dimension
        key1, key2 = jax.random.split(rng_key)
        samples = jax.random.uniform(key1, shape=(n_candidates, n_components))

        # Project to the simplex (sum to 1)
        samples = samples / jnp.sum(samples, axis=1, keepdims=True)

        # Convert to list of dictionaries
        candidates = []
        for i in range(n_candidates):
            comp = {k: float(samples[i, j]) for j, k in enumerate(self.composition_keys)}
            candidates.append(comp)

        return candidates

    def generate_exploration_candidates(
        self,
        n_candidates: int,
        exploration_rate: float = 0.8,
        rng_key: Optional[jax.random.PRNGKey] = None,
    ) -> List[Dict[str, float]]:
        """
        Generate candidates focused on exploration.

        Args:
            n_candidates: Number of candidates to generate
            exploration_rate: How much to prioritize exploration (0-1)
            rng_key: JAX random key

        Returns:
            List of composition dictionaries
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        # Split between diverse and random candidates
        n_diverse = int(n_candidates * exploration_rate)
        n_random = n_candidates - n_diverse

        key1, key2 = jax.random.split(rng_key)

        # Generate diverse candidates
        diverse_candidates = self.generate_diverse_candidates(n_diverse, key1)

        # Generate random candidates
        random_candidates = []
        for _ in range(n_random):
            # Generate random weights that sum to 1
            weights = np.random.dirichlet(np.ones(len(self.composition_keys)))
            comp = {k: float(w) for k, w in zip(self.composition_keys, weights)}
            random_candidates.append(comp)

        return diverse_candidates + random_candidates

    def generate_exploitation_candidates(
        self,
        n_candidates: int,
        best_compositions: Dict[str, Dict[str, float]],
        rng_key: Optional[jax.random.PRNGKey] = None,
    ) -> List[Dict[str, float]]:
        """
        Generate candidates focused on exploiting promising regions.

        Args:
            n_candidates: Number of candidates to generate
            best_compositions: Dictionary mapping property names to best compositions
            rng_key: JAX random key

        Returns:
            List of composition dictionaries
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        # If no best compositions yet, fall back to exploration
        if not best_compositions:
            return self.generate_exploration_candidates(n_candidates, 0.5, rng_key)

        # Generate candidates around each best composition
        candidates = []

        # Extract best compositions as centers
        centers = list(best_compositions.values())

        # Add some random centers for diversity
        key1, key2 = jax.random.split(rng_key)
        random_centers = self.generate_diverse_candidates(3, key1)
        centers.extend(random_centers)

        # Calculate how many candidates per center
        n_per_center = n_candidates // len(centers)
        remaining = n_candidates % len(centers)

        for i, center in enumerate(centers):
            n_current = n_per_center + (1 if i < remaining else 0)

            # Generate perturbations around this center
            for _ in range(n_current):
                # Create perturbation
                perturbation = np.random.normal(0, 0.1, len(self.composition_keys))

                # Apply perturbation
                new_comp = {}
                for j, k in enumerate(self.composition_keys):
                    new_comp[k] = center.get(k, 0) + perturbation[j]

                # Ensure non-negative
                for k in new_comp:
                    new_comp[k] = max(0, new_comp[k])

                # Normalize to sum to 1
                total = sum(new_comp.values())
                if total > 0:
                    for k in new_comp:
                        new_comp[k] /= total

                candidates.append(new_comp)

        return candidates

    def generate_optimization_candidates(
        self,
        n_candidates: int,
        best_compositions: Dict[str, Dict[str, float]],
        rng_key: Optional[jax.random.PRNGKey] = None,
    ) -> List[Dict[str, float]]:
        """
        Generate candidates focused on fine-tuning the best compositions.

        Args:
            n_candidates: Number of candidates to generate
            best_compositions: Dictionary mapping property names to best compositions
            rng_key: JAX random key

        Returns:
            List of composition dictionaries
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        # If no best compositions yet, fall back to exploitation
        if not best_compositions:
            return self.generate_exploitation_candidates(n_candidates, {}, rng_key)

        # Similar to exploitation but with smaller perturbations
        candidates = []

        # Extract best compositions as centers
        centers = list(best_compositions.values())

        # Calculate how many candidates per center
        n_per_center = n_candidates // len(centers)
        remaining = n_candidates % len(centers)

        for i, center in enumerate(centers):
            n_current = n_per_center + (1 if i < remaining else 0)

            # Generate perturbations around this center
            for _ in range(n_current):
                # Create smaller perturbation for fine-tuning
                perturbation = np.random.normal(0, 0.05, len(self.composition_keys))

                # Apply perturbation
                new_comp = {}
                for j, k in enumerate(self.composition_keys):
                    new_comp[k] = center.get(k, 0) + perturbation[j]

                # Ensure non-negative
                for k in new_comp:
                    new_comp[k] = max(0, new_comp[k])

                # Normalize to sum to 1
                total = sum(new_comp.values())
                if total > 0:
                    for k in new_comp:
                        new_comp[k] /= total

                candidates.append(new_comp)

        return candidates

    def generate_balanced_candidates(
        self,
        n_candidates: int,
        exploration_rate: float = 0.5,
        best_compositions: Optional[Dict[str, Dict[str, float]]] = None,
        rng_key: Optional[jax.random.PRNGKey] = None,
    ) -> List[Dict[str, float]]:
        """
        Generate a balanced mix of exploration and exploitation candidates.

        Args:
            n_candidates: Number of candidates to generate
            exploration_rate: How much to prioritize exploration (0-1)
            best_compositions: Dictionary mapping property names to best compositions
            rng_key: JAX random key

        Returns:
            List of composition dictionaries
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        key1, key2 = jax.random.split(rng_key)

        # Split between exploration and exploitation
        n_explore = int(n_candidates * exploration_rate)
        n_exploit = n_candidates - n_explore

        # Generate exploration candidates
        explore_candidates = self.generate_exploration_candidates(n_explore, 0.8, key1)

        # Generate exploitation candidates
        if best_compositions:
            exploit_candidates = self.generate_exploitation_candidates(
                n_exploit, best_compositions, key2
            )
        else:
            # If no best compositions yet, just generate more exploration candidates
            exploit_candidates = self.generate_exploration_candidates(n_exploit, 0.5, key2)

        return explore_candidates + exploit_candidates

    def select_experiments(
        self,
        pred_means: np.ndarray,
        pred_vars: np.ndarray,
        n_experiments: int = 10,
        acquisition_function: str = "UCB",
        rng_key: Optional[jax.random.PRNGKey] = None,
    ) -> Tuple[List[int], np.ndarray]:
        """
        Select the most informative experiments using an acquisition function.

        Args:
            pred_means: Predicted means (n_candidates, n_properties)
            pred_vars: Predicted variances (n_candidates, n_properties)
            n_experiments: Number of experiments to select
            acquisition_function: Name of the acquisition function to use
            rng_key: JAX random key

        Returns:
            Tuple of (selected indices, acquisition scores)
        """
        if rng_key is None:
            rng_key = self.rng_key
            self.rng_key, rng_key = jax.random.split(self.rng_key)

        # Get acquisition function
        acq_fn = get_acquisition_function(acquisition_function)

        # Compute acquisition scores
        acquisition_kwargs = {
            "beta": self.config["active_learning"].get("ucb_beta", 2.0),
            "maximize": True,
            "rng_key": rng_key,
        }

        acquisition_scores = acq_fn(pred_means, pred_vars, **acquisition_kwargs)

        # Select top candidates
        selected_indices = np.argsort(acquisition_scores)[-n_experiments:]

        return selected_indices.tolist(), acquisition_scores
