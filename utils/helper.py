<<<<<<< HEAD
import os
import sys
from typing import List


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def print_header(title: str) -> None:
    print("=" * 60)
    print(title)
    print("=" * 60)


def prompt_float_input(prompt: str, min_val: float = None, max_val: float = None) -> float:
    while True:
        try:
            val = input(f"{prompt}: ")
            if val.strip() == "":
                print("Input cannot be empty")
                continue
            f = float(val)
            if (min_val is not None and f < min_val) or (max_val is not None and f > max_val):
                print(f"Value must be between {min_val} and {max_val}")
                continue
            return f
        except ValueError:
            print("Please enter a valid number.")


def prompt_menu_choice(prompt: str, options: List[str]) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in options:
            return choice
        print(f"Invalid choice. Choose from: {', '.join(options)}")
=======
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
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
