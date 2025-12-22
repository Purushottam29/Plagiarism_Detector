from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.core.config import settings
from app.services.nlp.nlp_pipeline import process_text
from app.services.nlp.text_store import save_sentences

router = APIRouter(prefix="/nlp", tags=["NLP"])


@router.post("/{file_id}")
async def run_nlp(file_id: str):
    text_file = settings.EXTRACTED_TEXT_DIR / f"{file_id}.txt"

    if not text_file.exists():
        raise HTTPException(status_code=404, detail="OCR text not found")

    sentences = process_text(text_file)
    output_path = save_sentences(file_id, sentences)

    return {
        "file_id": file_id,
        "sentences_count": len(sentences),
        "output_file": output_path.name
    }

