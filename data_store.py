"""อ่านและบันทึกประวัติการเรียนในไฟล์ JSON"""

import json
from pathlib import Path

Record = dict[str, str | int]
DATA_FILE = Path(__file__).with_name("study_records.json")


def load_records(file_path: str | Path | None = None) -> list[Record]:
    """อ่านประวัติจาก JSON และสร้างไฟล์ว่างเมื่อยังไม่มีไฟล์"""
    path = Path(file_path) if file_path is not None else DATA_FILE
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.write_text("[]\n", encoding="utf-8")
        return []

    with path.open("r", encoding="utf-8") as file:
        records = json.load(file)

    if not isinstance(records, list) or any(
        not isinstance(record, dict) for record in records
    ):
        raise ValueError("รูปแบบข้อมูลในไฟล์ JSON ไม่ถูกต้อง")

    return records


def save_record(record: Record, file_path: str | Path | None = None) -> None:
    """เพิ่มรายการเรียนและบันทึกประวัติทั้งหมดกลับลงใน JSON"""
    path = Path(file_path) if file_path is not None else DATA_FILE
    records = load_records(path)
    records.append(record)

    with path.open("w", encoding="utf-8") as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
        file.write("\n")
