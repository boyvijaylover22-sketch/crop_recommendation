# Smart Farming AI Assistant

A simple terminal-based AI assistant for crop recommendation. This project loads a trained ML model and provides crop predictions, stores cultivation records, and gives basic farming recommendations.

## Installation

1. Create and activate a Python virtual environment (recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Model files

Place your trained model artifacts in `Smart_Farming_AI/models/`:
- `crop_model.pkl` (or a similarly named model file)
- `scaler.pkl` (if used)
- `label_encoder.pkl` (if used)

The app will also check the project root for these files.

## Run

```bash
cd "d:\crop dataset\Smart_Farming_AI"
python app.py
```

Follow the on-screen menu to predict crops or view records.

## Project structure

- `app.py` — CLI entry point and menu
- `predictor.py` — model loader and prediction wrapper
- `preprocessing.py` — input validation and feature ordering
- `recommendations.py` — generate farming advice
- `record_manager.py` — save and display cultivation records
- `utils/helper.py` — small helper utilities
- `models/` — place your model files here
- `records/` — saved `cultivation_records.csv`

## License

MIT
