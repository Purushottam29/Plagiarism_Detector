import json
from pathlib import Path

from app.core.config import settings
from app.services.report.highlighter import highlight_sentences
from app.services.report.pdf_generator import generate_pdf
from app.services.report.report_builder import run_plagiarism_check


def run_plagiarism_for_file(file_id: str) -> dict:
    """
    Wraps existing plagiarism, highlight and PDF generation functions.
    """
    stem = Path(file_id).stem
    nlp_output_path = settings.NLP_OUTPUT_DIR / f"{stem}.json"

    with open(nlp_output_path, "r", encoding="utf-8") as handle:
        nlp_data = json.load(handle)

    report = run_plagiarism_check(nlp_data)
    matches = report["matches"]

    sentences = [m["sentence"] for m in matches]
    scores = [m["similarity"] for m in matches]
    highlighted_text = highlight_sentences(sentences, scores)

    pdf_path = generate_pdf(file_id, report["plagiarism_percentage"], highlighted_text)

    analysis = [
        {
            "sentence": m["sentence"],
            "similarity_score": m["similarity"],
            "is_plagiarized": m.get("plagiarized", False),
        }
        for m in matches
    ]

    return {
        "plagiarism_percentage": report["plagiarism_percentage"],
        "analysis": analysis,
        "pdf_path": pdf_path,
        "total_sentences": len(analysis),
        "plagiarized": sum(1 for item in analysis if item["is_plagiarized"]),
    }
