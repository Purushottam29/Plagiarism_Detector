def highlight_sentences(sentences: list[str], scores: list[float], threshold: float = 0.7):
    results = []

    for sentence, score in zip(sentences, scores):
        results.append({
            "sentence": sentence,
            "similarity_score": round(float(score), 3),
            "is_plagiarized": score >= threshold
        })

    return results

