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
                    "Date",
                    "Nitrogen",
                    "Phosphorus",
                    "Potassium",
                    "Temperature",
                    "Humidity",
                    "pH",
                    "Rainfall",
                    "Predicted Crop",
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
