from PyPDF2 import PdfReader
from app.utils.logger import logger
import os
from app.config.settings import settings

def extract_text(content: bytes, file_id: str) -> str:
    try:
        with open(f"{settings.OUTPUT_DIR}/{file_id}.pdf", "wb") as f:
            f.write(content)
        reader = PdfReader(f"{settings.OUTPUT_DIR}/{file_id}.pdf")
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        text_path = f"{settings.OUTPUT_DIR}/{file_id}.txt"
        with open(text_path, "w") as f:
            f.write(text)
        logger.info(f"Text extracted and saved to {text_path}")
        return text_path
    except Exception as e:
        logger.exception("Error extracting text from PDF")
        raise