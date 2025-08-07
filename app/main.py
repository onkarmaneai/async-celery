from fastapi import FastAPI
from app.controller import pdf_controller

app = FastAPI()

app.include_router(pdf_controller.router)