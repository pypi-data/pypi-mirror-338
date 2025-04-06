import flax.linen as nn
import jax
import jax.numpy as jnp
from typing import Sequence, Optional

"""
Model module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


class PredictionHead(nn.Module):
    """A simple MLP head for predicting material properties from embeddings."""

    hidden_dims: Sequence[int]
    output_dim: int
    dropout_rate: Optional[float] = 0.0
    predict_uncertainty: bool = False  # If True, outputs mean and log_variance

    @nn.compact
    def __call__(self, x: jnp.ndarray, training: bool) -> jnp.ndarray:
        """Forward pass through the prediction head.

        Args:
            x: Input embeddings (batch_size, embedding_dim).
            training: Whether the model is in training mode (for dropout).

        Returns:
            Predicted properties (batch_size, output_dim) or
            (mean, log_variance) if predict_uncertainty is True.
        """
        # Hidden layers
        for dim in self.hidden_dims:
            x = nn.Dense(features=dim)(x)
            x = nn.relu(x)
            if self.dropout_rate is not None and self.dropout_rate > 0.0:
                x = nn.Dropout(rate=self.dropout_rate, deterministic=not training)(x)

        # Output layer
        if self.predict_uncertainty:
            # Output mean and log variance for uncertainty estimation
            mean = nn.Dense(features=self.output_dim, name="mean_output")(x)
            log_variance = nn.Dense(features=self.output_dim, name="logvar_output")(x)
            # Optional: constrain log_variance (e.g., softplus) if needed
            # log_variance = nn.softplus(log_variance)
            return mean, log_variance
        else:
            # Deterministic output
            x = nn.Dense(features=self.output_dim)(x)
            return x
