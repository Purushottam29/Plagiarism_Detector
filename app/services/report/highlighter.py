def highlight_sentences(sentences, scores, threshold=0.20):

    highlighted_text = ""

    for sentence, score in zip(sentences, scores):

        if score >= threshold:
            highlighted_text += f'<span class="plagiarized">{sentence}</span> '
        else:
            highlighted_text += sentence + " "

    return highlighted_text
