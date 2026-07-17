import pickle
from pathlib import Path
from typing import Optional, Tuple

import numpy as np


class CropPredictor:
    """Load the trained model and make predictions."""

    def __init__(self, model_dir: Optional[Path] = None):
        base = Path(__file__).parent
        self.model_dir = (base / "models") if model_dir is None else Path(model_dir)
        self.model = None
        self.scaler = None
        self.encoder = None
        self._load_resources()

    def _find_file(self, names):
        """Search for a file in the models folder or the project root."""
        for name in names:
            p = self.model_dir / name
            if p.exists():
                return p
        for name in names:
            p = Path(__file__).parent / name
            if p.exists():
                return p
        return None

    def _load_resources(self):
        """Load the trained model and optional preprocessing objects."""
        model_path = self._find_file(["crop_model.pkl", "crop_recommendation_model.pkl"])
        scaler_path = self._find_file(["scaler.pkl", "standard_scaler.pkl"])
        encoder_path = self._find_file(["label_encoder.pkl", "encoder.pkl", "label_encoder.sav"])

        if model_path is None:
            raise FileNotFoundError(
                "Trained model not found. Place crop_model.pkl in the models folder or project root."
            )

        with model_path.open("rb") as handle:
            self.model = pickle.load(handle)

        if scaler_path is not None:
            with scaler_path.open("rb") as handle:
                self.scaler = pickle.load(handle)

        if encoder_path is not None:
            with encoder_path.open("rb") as handle:
                self.encoder = pickle.load(handle)

    def predict(self, features: np.ndarray | list[float]) -> Tuple[str, Optional[float]]:
        """Predict a crop and return a confidence score if available."""
        x = np.array(features, dtype=float)
        if x.ndim == 1:
            x = x.reshape(1, -1)

        if self.scaler is not None:
            try:
                x = self.scaler.transform(x)
            except Exception:
                pass

        pred_idx = self.model.predict(x)
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
