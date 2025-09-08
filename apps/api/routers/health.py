from fastapi import APIRouter
from core.logging.setup import get_logger

router = APIRouter()
logger = get_logger(__name__)

@router.get("/health")
async def health_check():
    logger.debug("Health check endpoint accessed")
    return {"status": "healthy"}