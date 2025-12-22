from pathlib import Path
from app.services.ingestion.file_router import detect_file_type
from app.services.ingestion.image_preprocessor import ImagePreprocessor
from app.services.ingestion.pdf_preprocessor import PDFPreprocessor

def ingest(file_path: Path) -> Path:
    file_type = detect_file_type(file_path)

    if file_type == "image":
        processor = ImagePreprocessor()
    elif file_type == "pdf":
        processor = PDFPreprocessor()
    else:
        raise ValueError("DOCX support coming next")

    return processor.process(file_path)

