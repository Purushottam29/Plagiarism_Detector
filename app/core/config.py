from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    APP_NAME: str = "Plagiarism Detection API"
    ENV: str = "development"
    DEBUG: bool = True

    BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    UPLOAD_DIR: Path = DATA_DIR / "uploads"
    EXTRACTED_TEXT_DIR: Path = DATA_DIR / "extracted_text"

    class Config:
        env_file = ".env"

settings = Settings()
