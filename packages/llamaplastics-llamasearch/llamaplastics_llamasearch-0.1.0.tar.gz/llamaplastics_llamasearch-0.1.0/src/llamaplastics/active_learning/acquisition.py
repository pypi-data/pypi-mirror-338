import jax
import jax.numpy as jnp
import numpy as np
from typing import Callable, Optional
import logging

"""
Acquisition module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


def get_acquisition_function(name: str) -> Callable:
    """Returns the specified acquisition function.

    Args:
        name: Name of the acquisition function ('UCB', 'Random', 'ExpectedImprovement', etc.).

    Returns:
        The corresponding acquisition function.
    """
    if name.lower() == "ucb":
        return upper_confidence_bound
    elif name.lower() == "random":
        return random_acquisition
    # Add EI, PI, etc. here
    # elif name.lower() == 'ei' or name.lower() == 'expectedimprovement':
    #     return expected_improvement
    # elif name.lower() == 'pi' or name.lower() == 'probabilityofimprovement':
    #     return probability_of_improvement
    else:
        logger.warning(f"Unknown acquisition function: {name}. Defaulting to UCB.")
        return upper_confidence_bound


def upper_confidence_bound(
    pred_means: np.ndarray,
    pred_vars: np.ndarray,
    beta: float = 2.0,
    maximize: bool = True,
    property_index: Optional[int] = None,
    **kwargs,  # Consume unused args like rng_key
) -> np.ndarray:
    """Calculate the Upper Confidence Bound (UCB) acquisition score.

    Args:
        pred_means: Predicted means (n_candidates, n_properties).
        pred_vars: Predicted variances (n_candidates, n_properties).
        beta: Exploration-exploitation trade-off parameter.
        maximize: Whether the objective is to maximize (True) or minimize (False).
        property_index: Index of the property to optimize (if None, uses mean across properties).

    Returns:
        UCB scores for each candidate (n_candidates,).
    """
    pred_std = np.sqrt(pred_vars)

    # Select property or use mean across properties
    if property_index is not None:
        means = pred_means[:, property_index]
        stds = pred_std[:, property_index]
    else:
        # Aggregate across properties (e.g., mean)
        # Note: Averaging means and stds might not be ideal for multi-objective.
        # Consider specific multi-objective acquisition functions.
        means = np.mean(pred_means, axis=1)
        stds = np.mean(pred_std, axis=1)

    sign = 1.0 if maximize else -1.0
    ucb_scores = sign * means + beta * stds
    return ucb_scores


def random_acquisition(
    pred_means: np.ndarray,
    pred_vars: np.ndarray,
    rng_key: Optional[jax.random.PRNGKey] = None,
    **kwargs,  # Consume unused args
) -> np.ndarray:
    """Assign random acquisition scores for random selection.

    Args:
        pred_means: Predicted means (n_candidates, n_properties).
        pred_vars: Predicted variances (n_candidates, n_properties).
        rng_key: JAX random key for generating random scores.

    Returns:
        Random scores for each candidate (n_candidates,).
    """
    n_candidates = pred_means.shape[0]
    if rng_key is None:
        # Use numpy random if no JAX key provided (e.g., during planning)
        return np.random.rand(n_candidates)
    else:
        # Use JAX random if key is provided
        return jax.random.uniform(rng_key, shape=(n_candidates,))


# --- Placeholder for other acquisition functions ---

# def expected_improvement(...):
#     pass

# def probability_of_improvement(...):
#     pass
