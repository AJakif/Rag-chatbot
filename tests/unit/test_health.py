from fastapi.testclient import TestClient
from apps.api.main import app
from core.logging.setup import get_logger

client = TestClient(app)
logger = get_logger(__name__)

def test_health_endpoint():
    logger.info("Testing health endpoint")
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
    logger.debug("Health endpoint test completed")

def test_root_endpoint():
    logger.info("Testing root endpoint")
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "environment" in data
    logger.debug("Root endpoint test completed")