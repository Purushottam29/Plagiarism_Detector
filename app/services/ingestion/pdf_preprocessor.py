from pathlib import Path
from app.services.ingestion.preprocessor import BasePreprocessor

class PDFPreprocessor(BasePreprocessor):

    def process(self, file_path: Path) -> Path:
        # Placeholder
        # Later: convert PDF pages to images
        return file_path

