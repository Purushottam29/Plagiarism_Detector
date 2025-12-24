from pathlib import Path
import fitz  # PyMuPDF
from app.core.config import settings
from app.services.ingestion.ocr_pipeline import process_image_for_ocr
import uuid


class PDFPreprocessor:
    def process(self, pdf_path: Path) -> Path:
        doc = fitz.open(pdf_path)
        extracted_text = []

        for page_index, page in enumerate(doc):
            page_text = page.get_text().strip()

            # Extract text layer if present
            if page_text:
                extracted_text.append(page_text)

            # Extract images and OCR them
            images = page.get_images(full=True)

            for img_index, img in enumerate(images):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]

                image_name = (
                    f"{pdf_path.stem}_p{page_index}_img_{uuid.uuid4().hex}.png"
                )
                image_path = settings.UPLOAD_DIR / image_name

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                ocr_text = process_image_for_ocr(image_path)
                if ocr_text.strip():
                    extracted_text.append(ocr_text)

    # Write final merged text
        output_path = settings.EXTRACTED_TEXT_DIR / f"{pdf_path.stem}.txt"
        output_path.write_text("\n".join(extracted_text), encoding="utf-8")

        return output_path

