# Smart Farming AI Assistant

This project provides a beginner-friendly crop prediction assistant powered by a trained machine learning model.

## Features
- Predict the most suitable crop from soil and environmental inputs
- Display prediction confidence when available
- Save each prediction in a CSV file
- View previous cultivation records
- Provide simple farming recommendations

## Installation
1. Create and activate a Python environment.
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Run the Application
```bash
python app.py
```

## Project Structure
- app.py: Main menu and user interaction
- predictor.py: Loads the trained model and returns predictions
- preprocessing.py: Validates and prepares user inputs
- recommendations.py: Creates farming recommendations
- record_manager.py: Stores and reads CSV records
- models/: Contains the trained model and preprocessing artifacts
- records/: Stores cultivation records

## Example
When the app starts, choose option 1 and enter values such as:
- Nitrogen: 90
- Phosphorus: 42
- Potassium: 43
- Temperature: 24
- Humidity: 60
- pH: 6.5
- Rainfall: 120
