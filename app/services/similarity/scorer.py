import numpy as np

def plagiarism_score(similarity_matrix: np.ndarray, threshold: float = 0.7):
    matches = similarity_matrix.max(axis=1)
    plagiarized = matches >= threshold

    percentage = (plagiarized.sum() / len(matches)) * 100
    return percentage, matches

