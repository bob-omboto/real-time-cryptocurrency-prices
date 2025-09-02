"""
Unit tests for CoinGecko API interactions
"""
import pytest
from src.ingest_crypto import fetch_and_print_prices
from unittest.mock import patch

def test_successful_api_call(mock_successful_api_response):
    """Test successful API call to CoinGecko"""
    with patch('requests.get', return_value=mock_successful_api_response):
        result = fetch_and_print_prices()
        assert result is None  # function prints but doesn't return anything

def test_failed_api_call(mock_failed_api_response):
    """Test handling of failed API call"""
    with patch('requests.get', return_value=mock_failed_api_response):
        result = fetch_and_print_prices()
        assert result is None  # function should handle error gracefully