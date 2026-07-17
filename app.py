import sys
from datetime import datetime

from colorama import Fore, Style, init

from predictor import CropPredictor
from preprocessing import InputValidationError, preprocess_inputs
from record_manager import RecordManager
from recommendations import RecommendationEngine
from utils.helper import clear_screen, print_header, prompt_float_input, prompt_menu_choice


def show_menu() -> None:
    print_header("Smart Farming AI Assistant")
    print("1. Predict Crop")
    print("2. View Cultivation Records")
    print("3. Exit")
    print()


def get_soil_inputs() -> dict:
    print_header("Enter Soil and Environmental Values")
    inputs = {
        "N": prompt_float_input("Nitrogen (N)", 0.0, 300.0),
        "P": prompt_float_input("Phosphorus (P)", 0.0, 300.0),
        "K": prompt_float_input("Potassium (K)", 0.0, 300.0),
        "temperature": prompt_float_input("Temperature (°C)", -10.0, 60.0),
        "humidity": prompt_float_input("Humidity (%)", 0.0, 100.0),
        "ph": prompt_float_input("Soil pH", 0.0, 14.0),
        "rainfall": prompt_float_input("Rainfall (mm)", 0.0, 1000.0),
    }
    return inputs


def display_prediction(prediction: str, confidence: float, explanation: str) -> None:
    print_header("Prediction Result")
    print(f"{Fore.GREEN}Predicted crop:{Style.RESET_ALL} {prediction}")
    if confidence is not None:
        print(f"{Fore.CYAN}Confidence:{Style.RESET_ALL} {confidence:.2%}")
    print(f"{Fore.YELLOW}Why this crop is suitable:{Style.RESET_ALL} {explanation}")
    print()


def main() -> None:
    init(autoreset=True)
    predictor = CropPredictor()
    recommender = RecommendationEngine()
    record_manager = RecordManager()

    while True:
        clear_screen()
        show_menu()
        choice = prompt_menu_choice("Please select an option (1-3): ", ["1", "2", "3"])

        if choice == "1":
            try:
                user_inputs = get_soil_inputs()
                processed_inputs = preprocess_inputs(user_inputs)
                prediction, confidence = predictor.predict(processed_inputs)
                explanation = recommender.generate(prediction, processed_inputs)
                display_prediction(prediction, confidence, explanation)
                record_manager.save_record(
                    processed_inputs, prediction, confidence, datetime.now()
                )
                input("Press Enter to return to the main menu...")
            except InputValidationError as exc:
                print(f"{Fore.RED}Input error:{Style.RESET_ALL} {exc}")
                input("Press Enter to retry...")
            except Exception as exc:
                print(f"{Fore.RED}Unexpected error:{Style.RESET_ALL} {exc}")
                input("Press Enter to return to the main menu...")

        elif choice == "2":
            clear_screen()
            record_manager.display_records()
            input("Press Enter to return to the main menu...")

        elif choice == "3":
            print(f"{Fore.GREEN}Thank you for using Smart Farming AI. Goodbye!{Style.RESET_ALL}")
            sys.exit(0)


if __name__ == "__main__":
    main()
