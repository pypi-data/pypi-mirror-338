import os
import logging
import yaml
import argparse
import numpy as np
import jax
from datetime import datetime
import pickle

"""
Main Agent module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


# Import project modules
# Need to ensure PYTHONPATH includes the project root or adjust imports
try:
    from llm_interface.embedder import LLMEmbedder
    from composition_encoding.encoder import (
        format_composition_prompt,
    )  # Assuming this function exists
    from property_predictor.model import PredictionHead
    from active_learning.loop import DataStore  # Assuming this class exists
    from robotics_interface.simulator_api import RoboticsSimulatorAPI  # Assuming this class exists
    from agent.agent import DiscoveryAgent
except ImportError as e:
    print(f"Error importing project modules: {e}")
    print("Ensure PYTHONPATH is set correctly or run from the project root.")

    # Define dummy classes/functions if imports fail for basic script structure
    class LLMEmbedder:
        pass

    def format_composition_prompt(*args):
        return ""

    class PredictionHead:
        def __init__(self, *args, **kwargs):
            pass

        def apply(self, *args, **kwargs):
            return (np.array([[0.0]]), np.array([[0.0]]))  # mean, log_var

    class DataStore:
        def __init__(self, *args):
            pass

        def load(self, *args):
            pass

    class RoboticsSimulatorAPI:
        def __init__(self, *args):
            pass

        def run_experiment(self, *args):
            return {}

    class DiscoveryAgent:
        def __init__(self, *args, **kwargs):
            pass

        def run(self, *args):
            return {}


# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def load_config(config_path: str):
    """Load configuration from YAML file."""
    try:
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found: {config_path}")
        raise
    except yaml.YAMLError as e:
        logger.error(f"Error parsing configuration file {config_path}: {e}")
        raise


def initialize_rng(seed: int):
    """Initialize JAX random number generator."""
    return jax.random.PRNGKey(seed)


def create_predictor_head_apply(config):
    """Create the JAX function to apply the prediction head."""
    try:

        def create_model():
            return PredictionHead(
                hidden_dims=config["predictor_head"]["hidden_dims"],
                output_dim=config["predictor_head"]["output_dim"],
                dropout_rate=config["predictor_head"]["dropout_rate"],
                predict_uncertainty=config["predictor_head"]["use_uncertainty"],
            )

        # Create a JAX-transformed apply function
        model = create_model()
        # Ensure model instance is available for apply
        # Note: Direct return of model.apply might lose 'self' context if needed internally.
        # If model.apply needs the instance, wrap it.
        # For Flax, using model instance directly in agent might be cleaner.
        # Here, returning the method assuming it's bound or static-like.
        return model.apply
    except KeyError as e:
        logger.error(f"Missing key in predictor_head config: {e}")
        raise


def train_head_fn(embeddings, properties, rng_key, config=None):
    """Function to train the prediction head."""
    # This is a complex function, importing locally to avoid top-level errors if deps missing
    try:
        import optax
        from flax.training import train_state
    except ImportError as e:
        logger.error(f"Missing dependency for training: {e}. Install optax and flax.")
        raise

    if config is None:
        logger.error("Training configuration (config) is required for train_head_fn")
        raise ValueError("Training configuration missing")

    # --- Model Creation ---
    try:
        model = PredictionHead(
            hidden_dims=config["predictor_head"]["hidden_dims"],
            output_dim=config["predictor_head"]["output_dim"],
            dropout_rate=config["predictor_head"]["dropout_rate"],
            predict_uncertainty=config["predictor_head"]["use_uncertainty"],
        )
    except KeyError as e:
        logger.error(f"Missing key in predictor_head config during training: {e}")
        raise

    # --- Data Preparation ---
    try:
        embeddings_jnp = jnp.array(embeddings)
        properties_jnp = jnp.array(properties)

        n_samples = embeddings.shape[0]
        if n_samples < 2:  # Need at least one for train and one for val
            logger.warning("Very few samples for training (< 2). Using all for training.")
            train_idx = jnp.arange(n_samples)
            val_idx = jnp.array([], dtype=jnp.int32)
        else:
            indices = jnp.arange(n_samples)
            rng_key, split_key = jax.random.split(rng_key)
            # Simple 80/20 split for validation during retraining
            train_idx, val_idx = jax.random.split(split_key, int(0.8 * n_samples))
            # Ensure indices are unique and cover the range (jax.random.split might not guarantee this)
            # A better approach uses train_test_split logic
            permuted_indices = jax.random.permutation(split_key, indices)
            split_point = int(0.8 * n_samples)
            train_idx = permuted_indices[:split_point]
            val_idx = permuted_indices[split_point:]
            if len(val_idx) == 0:  # Ensure val set is not empty if possible
                if len(train_idx) > 1:
                    val_idx = train_idx[-1:]
                    train_idx = train_idx[:-1]
                else:  # Cannot create val set
                    val_idx = jnp.array([], dtype=jnp.int32)
                    logger.warning("Could not create validation set with current data.")

    except Exception as e:
        logger.error(f"Error preparing data for training: {e}", exc_info=True)
        raise

    # --- Optimizer Setup ---
    try:
        num_epochs = config["training"]["num_epochs"]
        batch_size = config["training"]["batch_size"]
        learning_rate = config["training"]["learning_rate"]
        weight_decay = config["training"]["weight_decay"]

        steps_per_epoch = max(1, len(train_idx) // batch_size)
        total_steps = num_epochs * steps_per_epoch
        warmup_steps = min(100, total_steps // 10)  # Example: 10% warmup

        lr_schedule = optax.warmup_cosine_decay_schedule(
            init_value=0.0,
            peak_value=learning_rate,
            warmup_steps=warmup_steps,
            decay_steps=total_steps - warmup_steps,
            end_value=learning_rate / 10,
        )

        optimizer = optax.adamw(learning_rate=lr_schedule, weight_decay=weight_decay)
    except KeyError as e:
        logger.error(f"Missing key in training config: {e}")
        raise

    # --- Model Initialization ---
    try:
        rng_key, init_key = jax.random.split(rng_key)
        dummy_input = jnp.ones((1, embeddings.shape[1]))
        params = model.init(init_key, dummy_input, training=False)["params"]  # Extract params dict

        # Create train state
        state = train_state.TrainState.create(apply_fn=model.apply, params=params, tx=optimizer)
    except Exception as e:
        logger.error(f"Error initializing model or train state: {e}", exc_info=True)
        raise

    # --- Loss Function ---
    def loss_fn(params, x, y, rng_key, training=True):
        # Renamed internal config access for clarity
        predictor_config = config["predictor_head"]
        if predictor_config["use_uncertainty"]:
            mean, log_var = model.apply(
                {"params": params},
                x,
                training=training,
                rngs={"dropout": rng_key} if training else None,
            )
            precision = jnp.exp(-log_var)
            squared_error = jnp.square(y - mean)
            loss = 0.5 * (log_var + squared_error * precision)
            mask = ~jnp.isnan(y)
            loss = jnp.where(mask, loss, 0.0)
            n_valid = jnp.sum(mask, axis=0)  # Sum per property
            # Average over samples, then sum over properties (or mean if desired)
            loss_per_prop = jnp.sum(loss, axis=0) / jnp.maximum(n_valid, 1.0)
            total_loss = jnp.mean(loss_per_prop)  # Mean loss across properties

            mse = jnp.where(mask, squared_error, 0.0)
            rmse_per_prop = jnp.sqrt(jnp.sum(mse, axis=0) / jnp.maximum(n_valid, 1.0))
            mean_rmse = jnp.mean(rmse_per_prop)

            return total_loss, (mean_rmse, mean, log_var)
        else:
            preds = model.apply(
                {"params": params},
                x,
                training=training,
                rngs={"dropout": rng_key} if training else None,
            )
            mask = ~jnp.isnan(y)
            squared_error = jnp.square(y - preds)
            mse = jnp.where(mask, squared_error, 0.0)
            n_valid = jnp.sum(mask, axis=0)
            mse_per_prop = jnp.sum(mse, axis=0) / jnp.maximum(n_valid, 1.0)
            total_loss = jnp.mean(mse_per_prop)
            mean_rmse = jnp.sqrt(total_loss)
            return total_loss, (mean_rmse, preds)

    # --- Training Step Definition ---
    @jax.jit
    def train_step(state, batch, rng_key):
        x, y = batch
        rng_key, dropout_key = jax.random.split(rng_key)
        grad_fn = jax.value_and_grad(loss_fn, has_aux=True)
        (loss, aux), grads = grad_fn(state.params, x, y, dropout_key, training=True)
        new_state = state.apply_gradients(grads=grads)
        return new_state, loss, aux, rng_key

    # --- Eval Step Definition ---
    @jax.jit
    def eval_step(state, batch, rng_key):
        x, y = batch
        loss, aux = loss_fn(state.params, x, y, rng_key, training=False)
        return loss, aux

    # --- Training Loop ---
    logger.info(f"Starting training for {num_epochs} epochs...")
    metrics_history = []
    for epoch in range(num_epochs):
        rng_key, perm_key = jax.random.split(rng_key)
        permuted_train_idx = jax.random.permutation(perm_key, train_idx)

        epoch_losses = []
        for i in range(0, len(permuted_train_idx), batch_size):
            batch_indices = permuted_train_idx[i : i + batch_size]
            if len(batch_indices) == 0:
                continue

            x_batch = embeddings_jnp[batch_indices]
            y_batch = properties_jnp[batch_indices]

            state, loss, aux, rng_key = train_step(state, (x_batch, y_batch), rng_key)
            epoch_losses.append(loss)

        train_loss_epoch = jnp.mean(jnp.array(epoch_losses)) if epoch_losses else 0.0

        # Evaluation
        if len(val_idx) > 0 and (
            epoch % config["training"]["eval_frequency"] == 0 or epoch == num_epochs - 1
        ):
            val_x = embeddings_jnp[val_idx]
            val_y = properties_jnp[val_idx]
            rng_key, eval_key = jax.random.split(rng_key)
            val_loss, val_aux = eval_step(state, (val_x, val_y), eval_key)
            val_rmse = val_aux[0]

            metrics = {
                "epoch": epoch,
                "train_loss": float(train_loss_epoch),
                "val_loss": float(val_loss),
                "val_rmse": float(val_rmse),  # Mean RMSE across properties
            }
            metrics_history.append(metrics)
            logger.info(
                f"Epoch {epoch}: train_loss={train_loss_epoch:.4f}, val_loss={val_loss:.4f}, val_rmse={val_rmse:.4f}"
            )
        elif epoch % config["training"]["eval_frequency"] == 0:  # Log train loss even if no val set
            metrics = {
                "epoch": epoch,
                "train_loss": float(train_loss_epoch),
                "val_loss": None,
                "val_rmse": None,
            }
            metrics_history.append(metrics)
            logger.info(f"Epoch {epoch}: train_loss={train_loss_epoch:.4f} (No validation set)")

    logger.info("Training finished.")
    return state.params, metrics_history


def main(args):
    try:
        # Load configuration
        config = load_config(args.config)

        # Add default agent config if not present
        config.setdefault(
            "agent",
            {
                "max_iterations": 50,
                "early_stopping_threshold": 0.95,
                "exploration_decay_rate": 0.05,
            },
        )

        # Set random seed
        seed = config.get("seed", 42)
        np.random.seed(seed)
        rng_key = initialize_rng(seed)

        # Create output directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(args.output_dir, f"agent_run_{timestamp}")
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Results will be saved to: {output_dir}")

        # Save config
        config_save_path = os.path.join(output_dir, "config.yaml")
        try:
            with open(config_save_path, "w") as f:
                yaml.dump(config, f)
            logger.info(f"Configuration saved to {config_save_path}")
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")

        # Initialize LLM embedder
        logger.info("Initializing LLM embedder...")
        # Ensure cache dir exists
        embedder_cache = os.path.join(output_dir, "embeddings_cache")
        os.makedirs(embedder_cache, exist_ok=True)
        embedder = LLMEmbedder(
            model_name=config["llm"]["model_name"],
            embedding_layer=config["llm"]["embedding_layer"],
            device=config.get("device", "cpu"),
            cache_dir=embedder_cache,
        )

        # Create robotics simulator
        logger.info("Initializing Robotics Simulator...")
        robotics_api = RoboticsSimulatorAPI(config)

        # Create predictor head apply function
        logger.info("Creating Predictor Head function...")
        predictor_head_apply = create_predictor_head_apply(config)

        # Create or load data store
        data_store_path = args.data_store or os.path.join(output_dir, "data_store.pkl")
        data_store = DataStore(config["data"]["property_labels"])
        if os.path.exists(data_store_path) and args.data_store:
            logger.info(f"Loading existing data store from {data_store_path}")
            try:
                data_store.load(data_store_path)
            except Exception as e:
                logger.error(
                    f"Failed to load data store from {data_store_path}: {e}. Creating new one."
                )
        else:
            logger.info("Creating new data store")
            # Optional: Load initial data if specified and store doesn't exist/isn't loaded
            initial_data_path = config.get("data", {}).get("initial_dataset")
            if initial_data_path and os.path.exists(initial_data_path):
                logger.info(f"Loading initial data from {initial_data_path}")
                # Add logic here to load initial data (e.g., CSV) and add to data_store
                # Example:
                # import pandas as pd
                # initial_df = pd.read_csv(initial_data_path)
                # for _, row in initial_df.iterrows():
                #     comp = {k: row[k] for k in config["data"]["composition_keys"]}
                #     props = {p: row[p] for p in config["data"]["property_labels"]}
                #     data_store.add_data(comp, props)
                pass  # Placeholder for initial data loading

        # Create discovery agent
        logger.info("Initializing Discovery Agent...")
        agent = DiscoveryAgent(
            config=config,
            llm_embedder=embedder,
            predictor_head_apply=predictor_head_apply,
            experiment_runner=robotics_api.run_experiment,
            # Pass config to the training function via lambda
            train_head_fn=lambda emb, prop, rk: train_head_fn(emb, prop, rk, config=config),
            data_store=data_store,
            save_dir=output_dir,
        )

        # Run agent
        logger.info(f"Starting agent run for {args.num_iterations} iterations...")
        results = agent.run(args.num_iterations)

        # Save final results and data store
        final_results_path = os.path.join(output_dir, "final_results.pkl")
        final_datastore_path = os.path.join(output_dir, "final_data_store.pkl")
        try:
            with open(final_results_path, "wb") as f:
                pickle.dump(results, f)
            logger.info(f"Final results saved to {final_results_path}")
            data_store.save(final_datastore_path)
            logger.info(f"Final data store saved to {final_datastore_path}")
        except Exception as e:
            logger.error(f"Failed to save final results or data store: {e}")

        logger.info(f"Agent run completed. Results saved to {output_dir}")

        # Print summary
        print("\n--- Final Results Summary ---")
        if results and "state" in results:
            print(f"Total experiments: {results['state']['total_experiments']}")
            print("\nBest compositions found:")
            if "best_compositions" in results:
                for prop, comp in results["best_compositions"].items():
                    value = results.get("best_values", {}).get(prop, 0.0)
                    print(f"  {prop}: {value:.4f}")
                    if isinstance(comp, dict):
                        comp_str = ", ".join([f"{k}: {v:.2f}" for k, v in comp.items()])
                        print(f"    Composition: {comp_str}")
                    else:
                        print(f"    Composition: {comp}")  # Print if not dict
            else:
                print("  No best compositions recorded.")
        else:
            print("  Agent run did not produce expected results structure.")

    except Exception as e:
        logger.critical(f"An error occurred during the agent run: {e}", exc_info=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run autonomous discovery agent for LlamaPlastics")
    parser.add_argument(
        "--config",
        type=str,
        default="config.yaml",
        help="Path to config file (default: config.yaml)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="agent_results",
        help="Base directory for saving results (default: agent_results)",
    )
    parser.add_argument(
        "--data-store",
        type=str,
        default=None,
        help="Path to load an existing data store (.pkl file)",
    )
    parser.add_argument(
        "--num-iterations",
        type=int,
        default=20,
        help="Number of agent iterations to run (default: 20)",
    )

    args = parser.parse_args()
    main(args)
