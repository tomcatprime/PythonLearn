import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
SHEETY_TOKEN = os.getenv('SHEETY_TOKEN')
sheety_endpoint = f"https://api.sheety.co/{SHEETY_TOKEN}/flightDeals/prices"

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

class DataManager:
    
    def __init__(self):
        self.destination_data = {}
        
    
    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
                )
            
            
            
json_data = DataManager.get_destination_data()
print(json_data)
