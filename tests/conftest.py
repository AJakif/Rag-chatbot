import pytest
from fastapi.testclient import TestClient
from apps.api.main import app
from core.config.base import AppSettings
from core.logging.setup import setup_logging

@pytest.fixture(autouse=True)
def setup_test_environment():
    """Set up test environment before each test"""
    # Mock the settings
    test_settings = AppSettings(
        app_env="test",
        log_level="WARNING",  # Reduce log noise during tests
        log_path="./test_logs"
    )
    
    # Setup logging
    setup_logging(test_settings)

    # Set app settings
    app.state.settings = AppSettings()
    yield
    # Clean up after test
    if hasattr(app.state, "settings"):
        delattr(app.state, "settings")