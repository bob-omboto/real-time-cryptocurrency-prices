"""
Integration tests for the complete data pipeline
"""
import pytest
from ingest_crypto import main
from unittest.mock import patch
import asyncio

@pytest.mark.integration
async def test_full_pipeline():
    """Test the complete data pipeline"""
    with patch('src.ingest_crypto.fetch_and_send_prices') as mock_fetch:
        # Mock the main loop to run only once
        with patch('time.sleep', side_effect=KeyboardInterrupt):
            main()
            mock_fetch.assert_called_once()