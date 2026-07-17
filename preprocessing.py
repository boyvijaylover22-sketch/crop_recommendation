from typing import Dict, List

import numpy as np


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
