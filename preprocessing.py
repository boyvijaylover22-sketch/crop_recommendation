"""Input validation and preprocessing helpers for user-entered farm data."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any, Dict

import numpy as np


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
