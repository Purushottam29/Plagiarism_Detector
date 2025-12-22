from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.core.config import settings
from app.services.ingestion.ingestion_service import ingest

router = APIRouter(prefix="/ingest", tags=["Ingestion"])


@router.post("/{file_id}")
async def ingest_file(file_id: str):
    file_path = settings.UPLOAD_DIR / file_id

    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")

    try:
        processed_path = ingest(file_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return {
        "file_id": file_id,
        "processed_file": processed_path.name,
        "status": "ingested"
    }

