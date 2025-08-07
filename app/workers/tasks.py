from celery import Celery
from app.config.settings import settings
from app.services.pdf_service import extract_text
from app.utils.logger import logger
import os

os.makedirs(settings.OUTPUT_DIR, exist_ok=True)

celery_app = Celery(
    "tasks",
    broker=settings.BROKER_URL,
    backend=settings.RESULT_BACKEND
)

@celery_app.task
def extract_text_from_pdf(content: bytes, file_id: str) -> str:
    logger.info(f"Started processing file with ID: {file_id}")
    return extract_text(content, file_id)
