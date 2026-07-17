"""Helper utilities for the Smart Farming assistant."""

from __future__ import annotations


def format_confidence(confidence: float) -> str:
    """Format a confidence score as a percentage string."""
    return f"{confidence * 100:.2f}%"


def prompt_float(prompt: str, cancelable: bool = False) -> float | None:
    """Prompt a user for a numeric value and optionally allow cancellation."""
    while True:
        value = input(prompt).strip()
        if cancelable and value.lower() in {"q", "quit", "exit"}:
            return None

        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")
