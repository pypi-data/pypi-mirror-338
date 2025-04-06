import pickle
import logging
import os
import numpy as np
from typing import Dict, List, Any, Optional

"""
Loop module for llamaplastics_project.

This module provides functionality for the llamaplastics_project project.
"""


logger = logging.getLogger(__name__)


class DataStore:
    """Simple in-memory data store for active learning loop.
    Stores compositions and their corresponding measured properties.
    """

    def __init__(self, property_labels: List[str]):
        """Initialize the DataStore.

        Args:
            property_labels: List of property names in the order they are stored.
        """
        self.compositions: List[Dict[str, float]] = []
        self.properties: List[List[Optional[float]]] = []
        self.property_labels = property_labels
        self.label_to_index = {label: i for i, label in enumerate(property_labels)}
        logger.info(f"DataStore initialized with properties: {property_labels}")

    def add_data(self, composition: Dict[str, float], properties: Dict[str, float]):
        """Add a new data point (composition and measured properties).

        Args:
            composition: Dictionary representing the material composition.
            properties: Dictionary of measured property values.
        """
        self.compositions.append(composition)

        # Ensure properties are added in the correct order based on labels
        prop_values = [None] * len(self.property_labels)
        for label, value in properties.items():
            if label in self.label_to_index:
                prop_values[self.label_to_index[label]] = float(value)  # Ensure float
            else:
                logger.warning(f"Property '{label}' not in defined property labels. Ignoring.")
        self.properties.append(prop_values)
        # logger.debug(f"Added data point. Total samples: {len(self)}")

    def get_compositions(self) -> List[Dict[str, float]]:
        """Return all stored compositions."""
        return self.compositions

    def get_properties(self) -> np.ndarray:
        """Return all stored properties as a NumPy array.
        Missing values will be represented as np.nan.
        """
        # Convert list of lists to NumPy array, handling None as np.nan
        return np.array(self.properties, dtype=np.float32)

    def save(self, filepath: str):
        """Save the data store contents to a file using pickle."""
        try:
            with open(filepath, "wb") as f:
                pickle.dump(
                    {
                        "compositions": self.compositions,
                        "properties": self.properties,
                        "property_labels": self.property_labels,
                    },
                    f,
                )
            logger.info(f"DataStore saved successfully to {filepath}")
        except (IOError, pickle.PicklingError) as e:
            logger.error(f"Error saving DataStore to {filepath}: {e}")

    def load(self, filepath: str):
        """Load data store contents from a file."""
        if not os.path.exists(filepath):
            logger.error(f"DataStore file not found: {filepath}")
            return
        try:
            with open(filepath, "rb") as f:
                data = pickle.load(f)

            # Validate loaded data keys
            required_keys = {"compositions", "properties", "property_labels"}
            if not required_keys.issubset(data.keys()):
                raise ValueError(f"DataStore file {filepath} is missing required keys.")

            # Validate property labels match
            if data["property_labels"] != self.property_labels:
                logger.warning(
                    f"Loaded DataStore property labels {data['property_labels']} do not match current labels {self.property_labels}. Using loaded labels."
                )
                self.property_labels = data["property_labels"]
                self.label_to_index = {label: i for i, label in enumerate(self.property_labels)}

            self.compositions = data["compositions"]
            self.properties = data["properties"]
            logger.info(
                f"DataStore loaded successfully from {filepath}. Contains {len(self)} samples."
            )

        except (IOError, pickle.UnpicklingError, EOFError, ValueError) as e:
            logger.error(f"Error loading DataStore from {filepath}: {e}")
            # Reset to empty state on load failure?
            # self.compositions = []
            # self.properties = []

    def __len__(self) -> int:
        """Return the number of data points stored."""
        return len(self.compositions)
