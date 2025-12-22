from pathlib import Path
from app.services.ingestion.ocr.ocr_service import run_ocr
from app.services.ingestion.text_store import save_extracted_text

def process_image_for_ocr(image_path: Path, file_id: str):
    extracted_text = run_ocr(image_path)
    return save_extracted_text(file_id, extracted_text)

