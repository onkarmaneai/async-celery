import os

class Settings:
    BROKER_URL: str = os.getenv("BROKER_URL", "redis://localhost:6379/0")
    RESULT_BACKEND: str = os.getenv("RESULT_BACKEND", "redis://localhost:6379/0")
    OUTPUT_DIR: str = os.getenv("OUTPUT_DIR", "output")

settings = Settings()
