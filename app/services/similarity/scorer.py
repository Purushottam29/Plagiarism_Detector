import numpy as np


def score_matches(similarity_matrix: np.ndarray, threshold: float = 0.7):
    if similarity_matrix is None or similarity_matrix.size == 0:
        return 0.0, np.array([])

    similarity_matrix = np.asarray(similarity_matrix)

    best_matches = similarity_matrix.max(axis=1)
    plagiarized = best_matches >= threshold

    percentage = (plagiarized.sum() / len(best_matches)) * 100
    return float(percentage), best_matches

