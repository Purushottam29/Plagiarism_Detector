def build_report(file_id: str, plagiarism_percentage: float, highlighted_sentences: list[dict]):
    return {
        "file_id": file_id,
        "plagiarism_percentage": round(plagiarism_percentage, 2),
        "analysis": highlighted_sentences
    }

