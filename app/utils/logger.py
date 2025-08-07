# utils/logger.py
import logging
import os
from datetime import datetime
from app.config.settings import settings

# Ensure output directory exists
os.makedirs(settings.OUTPUT_DIR, exist_ok=True)

log_filename = f"{settings.OUTPUT_DIR}/log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
