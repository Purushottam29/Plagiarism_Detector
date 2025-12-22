from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.services.nlp.nlp_pipeline import process_text
from app.services.similarity.plagiarism_pipeline import run_plagiarism

router = APIRouter(prefix="/plagiarism", tags=["Plagiarism"])


@router.post("/{file_id}")
async def check_plagiarism(file_id: str):
    text_file = settings.EXTRACTED_TEXT_DIR / f"{file_id}.txt"

    if not text_file.exists():
        raise HTTPException(status_code=404, detail="Text not found")

    sentences = process_text(text_file)
    score, matches = run_plagiarism(sentences)

    return {
        "file_id": file_id,
        "plagiarism_percentage": round(score, 2),
        "sentence_matches": matches
    }

