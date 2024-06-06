# First commit after vacation, back to learning

import requests

url = "https://api.openweathermap.org/data/2.5/weather"

api_key = ""

weather_params = {
    "lat": 44.426765,
    "lon": 26.102537,
    "appid": api_key,
    
}
response = requests.get(url, params=weather_params)
response.raise_for_status()

print(response.json())