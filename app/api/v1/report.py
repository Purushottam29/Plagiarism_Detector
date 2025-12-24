# app/api/v1/plagiarism.py

from fastapi import APIRouter, HTTPException
from pathlib import Path
import json

from app.core.config import settings
from app.services.report.report_builder import run_plagiarism_check

router = APIRouter(prefix="/plagiarism", tags=["Plagiarism"])


@router.post("/{file_id}")
async def run_plagiarism(file_id: str):
    """
    Plagiarism Detection Endpoint

    Expects:
    - NLP pipeline already executed
    - NLP output stored as JSON

    Returns:
    - Plagiarism percentage
    - Sentence-level similarity scores
    """

    file_id = file_id.lower()
    stem = Path(file_id).stem

    #  NLP output produced earlier
    nlp_output_path = settings.NLP_OUTPUT_DIR / f"{stem}.json"

    if not nlp_output_path.exists():
        raise HTTPException(
            status_code=404,
            detail="NLP output not found. Run NLP before plagiarism."
        )

    try:
        with open(nlp_output_path, "r", encoding="utf-8") as f:
            nlp_data = json.load(f)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to load NLP output: {e}"
        )

    # Run plagiarism logic
    report = run_plagiarism_check(nlp_data)

    return {
        "file_id": file_id,
        "plagiarism_percentage": report["plagiarism_percentage"],
        "sentence_matches": report["sentence_matches"],
        "status": "plagiarism_completed"
    }

