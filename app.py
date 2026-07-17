"""Main entry point for the Smart Farming AI Assistant."""

from __future__ import annotations

from colorama import Fore, Style, init

from predictor import CropPredictor
from preprocessing import InputPreprocessor
from recommendations import RecommendationEngine
from record_manager import RecordManager
from utils.helper import format_confidence, prompt_float

init(autoreset=True)


class SmartFarmingAssistant:
    """Interactive command-line assistant for crop prediction."""

    def __init__(self) -> None:
        self.predictor = CropPredictor()
        self.preprocessor = InputPreprocessor()
        self.recommender = RecommendationEngine()
        self.record_manager = RecordManager()

    def run(self) -> None:
        """Run the application menu loop."""
        print(f"{Fore.GREEN}Smart Farming AI Assistant{Style.RESET_ALL}")
        print("Welcome! Predict a crop and receive practical farming advice.\n")

        while True:
            self.show_menu()
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.handle_prediction()
            elif choice == "2":
                self.view_records()
            elif choice == "3":
                print(f"{Fore.YELLOW}Thank you for using the Smart Farming Assistant!{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}Please select a valid option.{Style.RESET_ALL}")

    def show_menu(self) -> None:
        """Display the available menu options."""
        print("1. Predict Crop")
        print("2. View Cultivation Records")
        print("3. Exit")

    def handle_prediction(self) -> None:
        """Collect user input, preprocess it, predict a crop, and save the result."""
        print(f"\n{Fore.CYAN}Crop Prediction Form{Style.RESET_ALL}")
        print("Enter the soil and environment values below.")
        print("Type 'q' at any prompt to cancel.\n")

        raw_inputs = {}
        for field in self.preprocessor.feature_order:
            value = prompt_float(f"{field}: ", cancelable=True)
            if value is None:
                print(f"{Fore.YELLOW}Prediction cancelled.{Style.RESET_ALL}")
                return
            raw_inputs[field] = value

        try:
            processed_features = self.preprocessor.prepare_features(raw_inputs)
            predicted_crop, confidence = self.predictor.predict(processed_features)
            explanation = self.recommender.explain_crop_suitability(predicted_crop, raw_inputs)
            recommendations = self.recommender.generate_recommendations(predicted_crop, raw_inputs)

            print(f"\n{Fore.GREEN}Predicted Crop: {predicted_crop}{Style.RESET_ALL}")
            if confidence is not None:
                print(f"Confidence: {format_confidence(confidence)}")
            print(f"Why this crop fits: {explanation}")
            print("\nRecommendations:")
            for key, message in recommendations.items():
                print(f"- {key.replace('_', ' ').title()}: {message}")

            record = {
                "Date": self.record_manager.current_timestamp(),
                "Nitrogen": raw_inputs["Nitrogen"],
                "Phosphorus": raw_inputs["Phosphorus"],
                "Potassium": raw_inputs["Potassium"],
                "Temperature": raw_inputs["Temperature"],
                "Humidity": raw_inputs["Humidity"],
                "pH": raw_inputs["pH"],
                "Rainfall": raw_inputs["Rainfall"],
                "Predicted Crop": predicted_crop,
            }
            self.record_manager.save_record(record)
            print(f"{Fore.BLUE}Prediction saved to cultivation records.{Style.RESET_ALL}")
        except ValueError as exc:
            print(f"{Fore.RED}{exc}{Style.RESET_ALL}")
        except Exception as exc:  # pragma: no cover - defensive logging
            print(f"{Fore.RED}Unexpected error: {exc}{Style.RESET_ALL}")

    def view_records(self) -> None:
        """Display all saved cultivation records."""
        records = self.record_manager.get_records()
        if not records:
            print(f"{Fore.YELLOW}No cultivation records found yet.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.CYAN}Cultivation Records{Style.RESET_ALL}")
        for record in records:
            print("-" * 60)
            print(f"Date: {record['Date']}")
            print(f"Crop: {record['Predicted Crop']}")
            print(
                f"Soil/Climate: N={record['Nitrogen']}, P={record['Phosphorus']}, "
                f"K={record['Potassium']}, Temp={record['Temperature']}, "
                f"Humidity={record['Humidity']}, pH={record['pH']}, Rainfall={record['Rainfall']}"
            )


if __name__ == "__main__":
    SmartFarmingAssistant().run()
