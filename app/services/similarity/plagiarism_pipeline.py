from pathlib import Path
from app.core.config import settings
from app.db.corpus_loader import load_corpus
from app.services.similarity.hybrid import HybridSimilarityEngine
from app.services.similarity.scorer import plagiarism_score

def run_plagiarism(sentences: list[str]):
    corpus = load_corpus(settings.DATA_DIR / "corpus")

    engine = HybridSimilarityEngine(alpha=0.6)
    similarity = engine.compute(sentences, corpus)

    score, matches = plagiarism_score(similarity)
    return score, matches.tolist()

