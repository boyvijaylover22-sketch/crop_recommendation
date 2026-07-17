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
