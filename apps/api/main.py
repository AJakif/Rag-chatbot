from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.config.base import AppSettings
from core.logging.setup import setup_logging, get_logger

# Configure logging
logger = get_logger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        # Startup
        app.state.settings = AppSettings()

        # Setup logging
        setup_logging(app.state.settings)
        logger.info(f"Starting RAG Chatbot in {app.state.settings.app_env} mode")
        logger.info(f"Qdrant configured at {app.state.settings.qdrant_url}")
        logger.info(f"Logging level set to {app.state.settings.log_level}")
    except Exception as e:
        logger.error(f"Error during startup: {str(e)}")

    try:
        yield
    except Exception as e:
        logger.error(f"Error during application runtime: {str(e)}")
    finally:
        try:
            # Shutdown
            logger.info("Shutting down RAG Chatbot")
        except Exception as e:
            logger.error(f"Error during shutdown: {str(e)}")

app = FastAPI(lifespan=lifespan, title="RAG Chatbot API")

@app.get("/")
async def root():
    logger.debug("Root endpoint accessed")
    return {"message": "RAG Chatbot API is running", "environment": app.state.settings.app_env}

# Include routers
from apps.api.routers import health
app.include_router(health.router, prefix="/api/v1")