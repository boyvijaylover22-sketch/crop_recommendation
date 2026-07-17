<<<<<<< HEAD
from typing import Dict, List
=======
"""Input validation and preprocessing helpers for user-entered farm data."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any, Dict
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)

import numpy as np


<<<<<<< HEAD
class InputValidationError(Exception):
    pass


FEATURE_ORDER: List[str] = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]


def _validate_value(name: str, value: float) -> float:
    try:
        v = float(value)
    except Exception:
        raise InputValidationError(f"{name} must be a number")

    if name in ["N", "P", "K"] and not (0 <= v <= 1000):
        raise InputValidationError(f"{name} seems out of realistic range (0-1000)")
    if name == "temperature" and not (-30 <= v <= 80):
        raise InputValidationError("temperature seems out of realistic range (-30 to 80°C)")
    if name == "humidity" and not (0 <= v <= 100):
        raise InputValidationError("humidity must be between 0 and 100")
    if name == "ph" and not (0 <= v <= 14):
        raise InputValidationError("pH must be between 0 and 14")
    if name == "rainfall" and not (0 <= v <= 10000):
        raise InputValidationError("rainfall seems out of realistic range")

    return v


def preprocess_inputs(data: Dict[str, float]):
    """Validate and return a numpy array in the expected feature order.

    Raises InputValidationError on invalid inputs.
    """
    features = []
    for key in FEATURE_ORDER:
        if key not in data:
            raise InputValidationError(f"Missing input: {key}")
        v = _validate_value(key, data[key])
        features.append(float(v))

    return np.array(features)
=======
class InputPreprocessor:
    """Validate and preprocess feature inputs to match the training pipeline."""

    def __init__(self) -> None:
        self.feature_order = [
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "pH",
            "Rainfall",
        ]
        self.scaler = self._load_pickle("models/scaler.pkl")
        self.encoder = self._load_pickle("models/encoder.pkl")

    def _load_pickle(self, relative_path: str) -> Any:
        """Load a model artifact from disk if it exists."""
        path = Path(__file__).resolve().parent / relative_path
        if not path.exists():
            return None
        with path.open("rb") as handle:
            return pickle.load(handle)

    def validate_inputs(self, raw_inputs: Dict[str, float]) -> None:
        """Ensure user-provided values are numeric and within a reasonable range."""
        for field in self.feature_order:
            if field not in raw_inputs:
                raise ValueError(f"Missing required field: {field}")

            value = raw_inputs[field]
            if not isinstance(value, (int, float)):
                raise ValueError(f"{field} must be numeric")

            if value < 0:
                raise ValueError(f"{field} cannot be negative")

        if raw_inputs["pH"] <= 0:
            raise ValueError("pH must be greater than zero")

    def prepare_features(self, raw_inputs: Dict[str, float]) -> list[float]:
        """Prepare a feature vector matching the model training format."""
        self.validate_inputs(raw_inputs)
        values = [float(raw_inputs[field]) for field in self.feature_order]

        if self.scaler is not None:
            values = self.scaler.transform([values])[0]

        if self.encoder is not None and hasattr(self.encoder, "transform"):
            return [float(v) for v in values]

        return [float(v) for v in values]
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
