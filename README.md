# Real-Time Cryptocurrency Price Dashboard

A real-time data pipeline that fetches cryptocurrency prices and visualizes them using Microsoft Fabric.

## Overview

This project creates an end-to-end data pipeline that:
1. Fetches real-time cryptocurrency prices from the CoinGecko API
2. Processes the data through Microsoft Fabric Event Hub
3. Visualizes the data in a real-time dashboard

## Features

- Real-time price tracking for multiple cryptocurrencies including:
  - Bitcoin
  - Ethereum
  - Tether
  - Binance Coin
  - USD Coin
  - Ripple
  - Cardano
  - Dogecoin
  - Solana
  - Tron
- Price updates every 5 seconds
- Secure credential management using Azure Key Vault
- Scalable data ingestion using Event Hub
- CI/CD pipeline using Azure DevOps

## Prerequisites

- Python 3.8 or higher
- Azure subscription
- Microsoft Fabric workspace
- CoinGecko API access (free tier)
- Visual Studio Code

## Project Structure

```
/crypto-ingestion-project/
│
├── .vscode/                    # VS Code configuration
│   ├── launch.json            # Debugger configurations
│   └── settings.json          # Workspace settings
│
├── .venv/                     # Python virtual environment
│
├── azure-pipelines/           # CI/CD configuration
│   └── azure-pipelines.yml    # Azure DevOps pipeline definition
│
├── src/
    ├── __init__.py
│   └── ingest_crypto.py       # Main application script
│
├── tests/                     # Test files
│   ├── __init__.py           # Makes the tests directory a Python package
│   ├── conftest.py           # pytest configurations and fixtures
│   ├── test_api.py           # Tests for API interactions
│   └── test_integration.py    # Integration tests
│
├── pytest.ini
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Setup and Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/crypto-ingestion-project.git
cd crypto-ingestion-project
```

2. Create and activate a Python virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

1. Set up the following environment variables:
```bash
KEY_VAULT_URI="https://your-key-vault.vault.azure.net/"
EVENT_HUB_CONNECTION_SECRET_NAME="your-secret-name"
EVENT_HUB_NAME="your-event-hub-name"
```

2. Configure VS Code debugger settings in `.vscode/launch.json` if needed.

## Usage

Run the data ingestion script:
```bash
python src/ingest_crypto.py
```

## Development

- Use VS Code's integrated debugger with the provided launch configurations
- Follow the CI/CD pipeline defined in `azure-pipelines.yml`
- Create feature branches for new development

## Testing

The project uses pytest for testing. Tests are organized in the `tests` directory:

- `test_api.py`: Unit tests for CoinGecko API interactions
- `test_integration.py`: Integration tests for the Event Hub pipeline

To run the tests:

```bash
# Install test dependencies
pip install pytest pytest-mock pytest-asyncio

# Run all tests
pytest

# Run specific test file
pytest tests/test_api.py

# Run with coverage report
pytest --cov=src tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.