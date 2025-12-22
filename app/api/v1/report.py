from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.services.nlp.nlp_pipeline import process_text
from app.services.similarity.plagiarism_pipeline import run_plagiarism
from app.services.report.highlighter import highlight_sentences
from app.services.report.report_builder import build_report

router = APIRouter(prefix="/plagiarism", tags=["Plagiarism"])


@router.post("/{file_id}")
async def check_plagiarism(file_id: str):
    text_file = settings.EXTRACTED_TEXT_DIR / f"{file_id}.txt"

    if not text_file.exists():
        raise HTTPException(status_code=404, detail="Text not found")

    sentences = process_text(text_file)
    plagiarism_pct, scores = run_plagiarism(sentences)

    highlighted = highlight_sentences(sentences, scores)
    report = build_report(file_id, plagiarism_pct, highlighted)

    return report

