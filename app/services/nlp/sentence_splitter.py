import spacy

_nlp = spacy.load("en_core_web_sm")

def split_into_sentences(text: str) -> list[str]:
    doc = _nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]

