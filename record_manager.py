import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import pandas as pd

RECORDS_DIR = Path(__file__).parent / "records"
RECORDS_FILE = RECORDS_DIR / "cultivation_records.csv"


class RecordManager:
    """Handles saving and viewing cultivation records."""

    def __init__(self):
        RECORDS_DIR.mkdir(exist_ok=True)
        if not RECORDS_FILE.exists():
            with open(RECORDS_FILE, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Date",
                    "Nitrogen",
                    "Phosphorus",
                    "Potassium",
                    "Temperature",
                    "Humidity",
                    "pH",
                    "Rainfall",
                    "Predicted Crop",
                    "Confidence",
                ])

    def save_record(self, inputs: Dict[str, float], predicted_crop: str, confidence: Optional[float], timestamp: Optional[datetime] = None):
        ts = (timestamp or datetime.now()).isoformat()
        row = [
            ts,
            inputs.get("N"),
            inputs.get("P"),
            inputs.get("K"),
            inputs.get("temperature"),
            inputs.get("humidity"),
            inputs.get("ph"),
            inputs.get("rainfall"),
            predicted_crop,
            f"{confidence:.4f}" if confidence is not None else "",
        ]
        with open(RECORDS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row)

    def display_records(self):
        try:
            df = pd.read_csv(RECORDS_FILE)
            if df.empty:
                print("No records found.")
                return
            print(df.to_string(index=False))
        except Exception as exc:
            print(f"Failed to read records: {exc}")
