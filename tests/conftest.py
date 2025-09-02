"""
pytest configuration file containing shared fixtures
"""
import pytest
import requests
from unittest.mock import Mock

@pytest.fixture
def mock_successful_api_response():
    """Fixture that returns a mock successful API response"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "bitcoin": {"usd": 50000.0},
        "ethereum": {"usd": 3000.0}
    }
    return mock_response

@pytest.fixture
def mock_failed_api_response():
    """Fixture that returns a mock failed API response"""
    mock_response = Mock()
    mock_response.status_code = 429
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
    return mock_response