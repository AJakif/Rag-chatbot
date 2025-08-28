import pytest
from fastapi.testclient import TestClient
from apps.api.main import app
from core.config.base import AppSettings

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment before each test"""
    # Mock the settings
    app.state.settings = AppSettings()
    yield
    # Clean up after test
    if hasattr(app.state, "settings"):
        delattr(app.state, "settings")