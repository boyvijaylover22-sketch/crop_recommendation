<<<<<<< HEAD
import pickle
from pathlib import Path
from typing import Optional, Tuple

import numpy as np

MODEL_NAMES = ["crop_model.pkl", "crop_recommendation_model.pkl", "crop_recommendation_model.pkl"]
SCALER_NAMES = ["scaler.pkl", "standard_scaler.pkl"]
ENCODER_NAMES = ["label_encoder.pkl", "encoder.pkl", "label_encoder.sav"]


class ModelLoadError(Exception):
    pass


class CropPredictor:
    """Loads a trained model, scaler and encoder once and provides predict()."""

    def __init__(self, model_dir: Optional[Path] = None):
        base = Path(__file__).parent
        self.model_dir = (base / "models") if model_dir is None else Path(model_dir)
        self.model = None
        self.scaler = None
        self.encoder = None
        self._load_resources()

    def _find_file(self, names):
        # check models directory first, then parent folder
        for name in names:
            p = self.model_dir / name
            if p.exists():
                return p
        for name in names:
            p = Path(__file__).parent.parent / name
            if p.exists():
                return p
        return None

    def _load_resources(self):
        model_path = self._find_file(MODEL_NAMES)
        scaler_path = self._find_file(SCALER_NAMES)
        encoder_path = self._find_file(ENCODER_NAMES)

        if model_path is None:
            raise ModelLoadError(
                "Trained model not found. Place the model file (e.g. crop_model.pkl) in Smart_Farming_AI/models or the project root."
            )

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

        if scaler_path is not None:
            with open(scaler_path, "rb") as f:
                self.scaler = pickle.load(f)

        if encoder_path is not None:
            with open(encoder_path, "rb") as f:
                self.encoder = pickle.load(f)

    def predict(self, features: np.ndarray) -> Tuple[str, Optional[float]]:
        """Predict the crop and return (label, confidence).

        Args:
            features: 1D or 2D numpy array of raw or preprocessed features.
        """
        x = np.array(features)
        if x.ndim == 1:
            x = x.reshape(1, -1)

        if self.scaler is not None:
            try:
                x = self.scaler.transform(x)
            except Exception:
                # assume already scaled
                pass

        pred_idx = self.model.predict(x)

        # decode label if encoder available
        label = str(pred_idx[0])
        if self.encoder is not None:
            try:
                label = self.encoder.inverse_transform(pred_idx)[0]
            except Exception:
                label = str(pred_idx[0])

        confidence = None
        if hasattr(self.model, "predict_proba"):
            try:
                proba = self.model.predict_proba(x)
                confidence = float(proba.max())
            except Exception:
                confidence = None

        return label, confidence
=======
"""Prediction logic for the crop recommendation assistant."""

from __future__ import annotations

import pickle
from pathlib import Path
from typing import Any, Tuple


class CropPredictor:
    """Load and use the saved machine learning model."""

    def __init__(self, model_path: str | None = None) -> None:
        base_dir = Path(__file__).resolve().parent
        candidate_paths = []
        if model_path:
            candidate_paths.append(Path(model_path))
        candidate_paths.extend(
            [
                base_dir / "models" / "crop_model.pkl",
                base_dir / "crop_recommendation_model.pkl",
            ]
        )

        self.model_path = None
        for candidate in candidate_paths:
            if candidate.exists():
                self.model_path = candidate
                break

        if self.model_path is None:
            raise FileNotFoundError("Model file not found in expected locations")

        self.model = self._load_model()

    def _load_model(self) -> Any:
        """Load the trained model artifact from disk."""
        if not self.model_path.exists():
            raise FileNotFoundError(f"Model file not found: {self.model_path}")

        with self.model_path.open("rb") as handle:
            return pickle.load(handle)

    def predict(self, features: list[float]) -> Tuple[str, float | None]:
        """Predict the crop and return the confidence score if available."""
        if not isinstance(features, list):
            raise ValueError("Features must be provided as a list of numbers")

        prediction = self.model.predict([features])[0]
        confidence = None
        if hasattr(self.model, "predict_proba"):
            probabilities = self.model.predict_proba([features])[0]
            confidence = float(max(probabilities))
        return str(prediction), confidence
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
