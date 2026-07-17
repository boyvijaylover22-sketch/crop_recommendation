<<<<<<< HEAD
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
=======
"""Manage cultivation prediction records in CSV format."""

from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, List


class RecordManager:
    """Store and retrieve cultivation predictions."""

    def __init__(self, records_dir: str | None = None) -> None:
        base_dir = Path(__file__).resolve().parent
        self.records_dir = Path(records_dir or base_dir / "records")
        self.records_dir.mkdir(parents=True, exist_ok=True)
        self.csv_path = self.records_dir / "cultivation_records.csv"

    def current_timestamp(self) -> str:
        """Return the current timestamp string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_record(self, record: Dict[str, object]) -> None:
        """Append one prediction record to the CSV file."""
        file_exists = self.csv_path.exists()
        with self.csv_path.open("a", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
                    "Date",
                    "Nitrogen",
                    "Phosphorus",
                    "Potassium",
                    "Temperature",
                    "Humidity",
                    "pH",
                    "Rainfall",
                    "Predicted Crop",
<<<<<<< HEAD
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
=======
                ],
            )
            if not file_exists:
                writer.writeheader()
            writer.writerow(record)

    def get_records(self) -> List[Dict[str, str]]:
        """Read all saved records from the CSV file."""
        if not self.csv_path.exists():
            return []

        with self.csv_path.open("r", newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))
>>>>>>> 05f08e4 (Initial Smart Farming AI assistant)
