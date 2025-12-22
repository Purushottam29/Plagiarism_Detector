from pathlib import Path
from app.core.config import settings

def save_sentences(file_id: str, sentences: list[str]) -> Path:
    output_path = settings.EXTRACTED_TEXT_DIR / f"{file_id}.sentences.txt"

    with output_path.open("w", encoding="utf-8") as f:
        for s in sentences:
            f.write(s + "\n")

    return output_path

