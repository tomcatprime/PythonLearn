import os
from dotenv import load_dotenv
import requests
from pprint import pprint
# class DataManager:
#     #This class is responsible for talking to the Google Sheet.
#     pass

load_dotenv()
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

sheety_endpoint = f"https://api.sheety.co/{SHEETY_TOKEN}/flightDeals/prices"

sheety_headers = sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

# sheety_params = {
    
# }

sheety_read_data = requests.get(url=sheety_endpoint, headers=sheety_headers, verify=False)
sheety_read_data.raise_for_status()
pprint(sheety_read_data.json())