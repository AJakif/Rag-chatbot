from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config.base import AppSettings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.state.settings = AppSettings()
    logger.info(f"Starting RAG Chatbot in {app.state.settings.app_env} mode")
    logger.info(f"Qdrant configured at {app.state.settings.qdrant_url}")
    yield
    # Shutdown
    logger.info("Shutting down RAG Chatbot")

app = FastAPI(lifespan=lifespan, title="RAG Chatbot API")

@app.get("/")
async def root():
    return {"message": "RAG Chatbot API is running", "environment": app.state.settings.app_env}

# Include routers
from apps.api.routers import health
app.include_router(health.router, prefix="/api/v1")