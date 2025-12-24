from app.services.similarity import compute_similarity


def run_plagiarism_check(nlp_result: dict) -> dict:
    """
    Takes NLP output and returns final plagiarism report.

    Expected NLP format:
    {
        "sentences": [...],
        "corpus_sentences": [...]
    }
    """

    sentences = nlp_result.get("sentences", [])
    corpus_sentences = nlp_result.get("corpus_sentences", [])

    if not sentences or not corpus_sentences:
        return {
            "plagiarism_percentage": 0,
            "sentence_matches": []
        }

    plagiarism_percentage, sentence_scores = compute_similarity(
        sentences,
        corpus_sentences
    )

    return {
        "plagiarism_percentage": plagiarism_percentage,
        "sentence_matches": sentence_scores
    }

