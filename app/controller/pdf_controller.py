from fastapi import APIRouter, UploadFile, File, HTTPException
from app.workers.tasks import extract_text_from_pdf
from app.utils.logger import logger
import uuid

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Invalid file format")
    try:
        content = await file.read()
        file_id = str(uuid.uuid4())
        result = extract_text_from_pdf.delay(content, file_id)
        logger.info(f"PDF uploaded and task submitted: {file.filename} -> Task ID: {result.id}")
        return {"message": "File received and task submitted", "task_id": result.id}
    except Exception as e:
        logger.exception("Error uploading file")
        raise HTTPException(status_code=500, detail=str(e))