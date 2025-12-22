from pathlib import Path
from app.services.nlp.text_cleaner import clean_text
from app.services.nlp.sentence_splitter import split_into_sentences

def process_text(text_file: Path) -> list[str]:
    raw_text = text_file.read_text(encoding="utf-8")

    cleaned = clean_text(raw_text)
    sentences = split_into_sentences(cleaned)

    return sentences

