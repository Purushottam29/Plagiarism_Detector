# app/main.py
print("Main app is loading")
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.v1.health import router as health_router
from app.api.v1.upload import router as upload_router
from app.api.v1.ingest import router as ingest_router
from app.api.v1.ocr import router as ocr_router
from app.api.v1.nlp import router as nlp_router

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(ingest_router)
app.include_router(ocr_router)
app.include_router(nlp_router)

@app.on_event("startup")
async def startup_event():
    settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    settings.EXTRACTED_TEXT_DIR.mkdir(parents=True, exist_ok=True)

