import configparser
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.eventhub import EventHubProducerClient, EventData
import requests, json, time
from datetime import datetime

import os


config = configparser.ConfigParser()
config.read("config.ini")

vault_url = config["KeyVault"]["vault_url"]
eventhub_name_secret = config["KeyVault"]["eventhub_name_secret"]
eventhub_string_secret = config["KeyVault"]["eventhub_string_secret"]

# Authenticate and fetch secrets
credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url=vault_url, credential=credential)

eventhub_name = secret_client.get_secret(eventhub_name_secret).value
connection_str = secret_client.get_secret(eventhub_string_secret).value

eventhub_name = os.environ.get('eventhubname')
eventhub_string = os.environ.get('eventhubstring')

if not eventhub_name or not eventhub_string:
    raise ValueError("Environment variables for Event Hub are not set.")
# Load config

# Initialize Event Hub producer
producer = EventHubProducerClient.from_connection_string(
    conn_str=connection_str,
    eventhub_name=eventhub_name
)

# API details
url = "https://api.coingecko.com/api/v3/simple/price"
params = {
    "ids": "bitcoin,ethereum,tether,binancecoin,usd-coin,ripple,cardano,dogecoin,solana,tron",
    "vs_currencies": "usd"
}

# Function to fetch and send prices
def fetch_and_send_prices():
    response = requests.get(url, params=params)
    data = response.json()

    events = []
    for crypto, info in data.items():
        price = info.get("usd")
        if price is None:
            print(f"Skipping {crypto}: 'usd' price not found")
            continue

        price_data = {
            "crypto": crypto,
            "price": price,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())
        }
        print(price_data)
        event_data = EventData(json.dumps(price_data))
        events.append(event_data)

    if events:
        with producer:
            producer.send_batch(events)
    else:
        print("No valid price data to send")


# Loop to continuously fetch and send data
while True:
    fetch_and_send_prices()
    time.sleep(20)
