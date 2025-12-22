from pathlib import Path
import cv2
from app.services.ingestion.preprocessor import BasePreprocessor

class ImagePreprocessor(BasePreprocessor):

    def process(self, file_path: Path) -> Path:
        img = cv2.imread(str(file_path), cv2.IMREAD_GRAYSCALE)

        if img is None:
            raise ValueError("Invalid image file")

        processed = cv2.threshold(
            img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        output_path = file_path.with_suffix(".processed.png")
        cv2.imwrite(str(output_path), processed)

        return output_path

