import logging
from typing import Dict, Any, Callable, Optional

"""
Executor module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


class ExperimentExecutor:
    """
    Executes experiments by interfacing with the robotics API.
    """

    def __init__(self, config: Dict[str, Any], experiment_runner: Callable):
        """
        Initialize the experiment executor.

        Args:
            config: Configuration dictionary
            experiment_runner: Function to run experiments
        """
        self.config = config
        self.experiment_runner = experiment_runner
        self.experiment_count = 0

        logger.info("Experiment Executor initialized")

    def run_experiment(
        self, composition: Dict[str, float], processing: Optional[Dict[str, Any]] = None
    ) -> Dict[str, float]:
        """
        Run an experiment with the given composition.

        Args:
            composition: Material composition
            processing: Processing parameters (optional)

        Returns:
            Dictionary of measured properties
        """
        self.experiment_count += 1
        logger.info(f"Running experiment #{self.experiment_count} with composition: {composition}")

        # Use default processing if not provided
        if processing is None:
            processing = {"processing_temp": 60, "drying_time": 24}

        # Run the experiment
        try:
            properties = self.experiment_runner(composition, processing)

            # Log results
            logger.info(f"Experiment #{self.experiment_count} results: {properties}")

            return properties

        except Exception as e:
            logger.error(f"Error running experiment: {e}")

            # Return dummy results in case of error
            dummy_results = {prop: 0.0 for prop in self.config["data"]["property_labels"]}
            return dummy_results
