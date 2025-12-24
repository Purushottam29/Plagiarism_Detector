from fastapi import APIRouter, HTTPException
from pathlib import Path

from app.core.config import settings
from app.services.plagiarism.plagiarism_service import run_plagiarism_check

router = APIRouter(prefix="/plagiarism", tags=["Plagiarism"])


@router.post("/{file_id}")
async def run_plagiarism(file_id: str):
    file_id = file_id.lower()
    stem = Path(file_id).stem

    nlp_output_path = settings.NLP_OUTPUT_DIR / f"{stem}.json"

    if not nlp_output_path.exists():
        raise HTTPException(
            status_code=404,
            detail="NLP output not found. Run NLP first."
        )

    report = run_plagiarism_check(nlp_output_path)

    return report

