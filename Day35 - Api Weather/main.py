# First commit after vacation, back to learning
import json
import requests

# Used API from https://www.weatherapi.com/
api_key = ""

api_open = ""

url_open = "https://api.openweathermap.org/data/2.5/forecast?" #openweather api
url_weatherapi = "https://api.weatherapi.com/v1//forecast.json" #weatherapi.com
weather_params = {
    "lat": 44.426765,
    "lon": 26.102537,
    "appid": api_open,
    "cnt": 4,
}

response = requests.get(url_open, params=weather_params)
json_data = response.json()
# print(json.dumps(json_data, indent=2))
print(json_data)