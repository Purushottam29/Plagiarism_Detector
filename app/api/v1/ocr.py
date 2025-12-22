from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.core.config import settings
from app.services.ingestion.ocr_pipeline import process_image_for_ocr

router = APIRouter(prefix="/ocr", tags=["OCR"])


@router.post("/{file_id}")
async def run_ocr_endpoint(file_id: str):
    stem = Path(file_id).stem
    image_path = settings.UPLOAD_DIR / f"{stem}.processed.png"

    if not image_path.exists():
        raise HTTPException(status_code=404, detail="Processed image not found")

    output_path = process_image_for_ocr(image_path, file_id)

    return {
        "file_id": file_id,
        "text_file": output_path.name,
        "status": "ocr_completed"
    }

