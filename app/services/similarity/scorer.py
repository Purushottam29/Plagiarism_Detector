import numpy as np

def score_matches(similarity_matrix, sentences, corpus, threshold=0.20):

    best_scores = similarity_matrix.max(axis=1)
    best_indices = similarity_matrix.argmax(axis=1)

    matches = []
    plagiarized_count = 0

    for i, score in enumerate(best_scores):

        is_plag = score >= threshold

        if is_plag:
            plagiarized_count += 1

        matches.append({
            "sentence": sentences[i],
            "matched_text": corpus[best_indices[i]],
            "similarity": float(score),
            "plagiarized": is_plag
        })

    plagiarism_percentage = (plagiarized_count / len(sentences)) * 100

    return plagiarism_percentage, matches
