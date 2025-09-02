"""
This script fetches real-time cryptocurrency prices from the CoinGecko API
and sends them to a Microsoft Fabric Event Hub.

It securely retrieves the Event Hub connection string from an Azure Key Vault
using Azure Identity for authentication.
"""

import os
import json
import time
import requests
from datetime import datetime
# from azure.eventhub import EventHubProducerClient, EventData
# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential

# --- Configuration ---
# It's best practice to set these as environment variables rather than hardcoding.
# KEY_VAULT_URI = os.environ.get("KEY_VAULT_URI", "https://<YOUR-KEY-VAULT-NAME>.vault.azure.net/")
# EVENT_HUB_CONNECTION_SECRET_NAME = os.environ.get("EVENT_HUB_CONNECTION_SECRET_NAME", "<YOUR-SECRET-NAME-FOR-EH-CONN-STRING>")
# EVENT_HUB_NAME = os.environ.get("EVENT_HUB_NAME", "<YOUR-EVENT-HUB-NAME>") # This is the specific Event Hub name, not the namespace

# CoinGecko API Details
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
API_PARAMS = {
    "ids": "bitcoin,ethereum,tether,binancecoin,usd-coin,ripple,cardano,dogecoin,solana,tron",
    "vs_currencies": "usd"
}

# def get_eventhub_connection_string(vault_uri, secret_name):
#     """
#     Authenticates to Azure Key Vault and retrieves the specified secret.
#
#     Args:
#         vault_uri (str): The URI of the Azure Key Vault.
#         secret_name (str): The name of the secret to retrieve.
#
#     Returns:
#         str: The value of the retrieved secret (Event Hub connection string).
#     """
#     print("Authenticating to Azure and creating Key Vault client...")
#     # DefaultAzureCredential will attempt to authenticate using multiple methods
#     # (e.g., environment variables, managed identity, Azure CLI) which is ideal for
#     # both local development and deployment in Azure.
#     credential = DefaultAzureCredential()
#     secret_client = SecretClient(vault_url=vault_uri, credential=credential)
#
#     print(f"Fetching secret '{secret_name}' from Key Vault: {vault_uri}")
#     try:
#         secret = secret_client.get_secret(secret_name)
#         print("Successfully retrieved secret from Key Vault.")
#         return secret.value
#     except Exception as e:
#         print(f"Error retrieving secret from Key Vault: {e}")
#         raise

def fetch_and_print_prices():
    """
    Fetches cryptocurrency prices from the CoinGecko API and prints them to the console.
    """
    try:
        response = requests.get(COINGECKO_API_URL, params=API_PARAMS, timeout=20)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        data = response.json()

        print("--- Fetched Prices ---")
        for crypto, info in data.items():
            price_data = {
                "crypto": crypto,
                "price": info["usd"],
                "timestamp": datetime.now().isoformat() #"timestamp": time.time()
            }
            print(f"Formatted data: {price_data}")
        print("----------------------\n")


    except requests.exceptions.RequestException as e:
        print(f"Error calling CoinGecko API: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to orchestrate the process.
    """
    try:
        # This is a simplified loop for local testing.
        # It calls the API and prints the data without sending to Event Hub.
        print("Starting the data ingestion loop for local testing. Press Ctrl+C to stop.")
        while True:
            fetch_and_print_prices()
            # Adjust the interval as needed
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nProcess stopped by user.")
    except Exception as e:
        print(f"A critical error occurred in the main loop: {e}")

if __name__ == "__main__":
    main()

