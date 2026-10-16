
import json
from pathlib import Path

FILE_DATA = Path(__file__).with_name("data_mahasiswa.json")


def baca_data(file_path=FILE_DATA):
    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def simpan_data(data, file_path=FILE_DATA):
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
