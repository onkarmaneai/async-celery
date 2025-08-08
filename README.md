# Async PDF Text Extractor

An async FastAPI application to upload PDF files, extract text using Celery workers, and save the output.

## Features
- Async PDF upload endpoint
- Celery-based text extraction worker
- Configurable Redis broker and backend
- Stores extracted text to file
- Detailed logging with timestamps and exceptions

## Project Structure
```
app/
├── main.py            # FastAPI app entry
├── controller/
│   └── pdf_controller.py   # Upload route
├── services/
│   └── pdf_service.py      # PDF processing logic
├── workers/
│   └── tasks.py            # Celery tasks
├── config/
│   └── settings.py         # Configs
├── utils/
│   └── logger.py           # Logger setup
├── output/                 # Storage for files & logs
requirements.txt
README.md
```

## Prerequisites
- Python 3.8+
- Redis running locally or remotely

## Install & Run

```bash
# Clone repo
cd async_pdf_extractor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Redis locally (optional)
redis-server

# Run FastAPI app
uvicorn app.main:app --reload

# Start Celery worker
celery -A app.workers.tasks.celery_app worker --loglevel=info
```

## Usage

Send a POST request:
```bash
curl -X POST "http://localhost:8000/upload" -F "file=@your_file.pdf"
```

Returns:
```json
{
  "message": "File received and task submitted",
  "task_id": "abc123..."
}
```

Text file saved in `output/` folder.
