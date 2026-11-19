"""ทดสอบการสร้างไฟล์และการเก็บประวัติ JSON"""

import json
import tempfile
import unittest
from pathlib import Path

from data_store import load_records, save_record


class DataStoreTests(unittest.TestCase):
    def test_creates_file_and_keeps_saved_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            file_path = Path(temporary_directory) / "study_records.json"
            record = {"subject": "ชีววิทยา", "minutes": 30, "category": "Medium"}

            self.assertEqual(load_records(file_path), [])
            self.assertTrue(file_path.exists())

            save_record(record, file_path)
            self.assertEqual(load_records(file_path), [record])

            with file_path.open("r", encoding="utf-8") as file:
                self.assertEqual(json.load(file), [record])


if __name__ == "__main__":
    unittest.main()
