# First commit after vacation, back to learning
import json
import requests
from twilio.rest import Client # API to send text message

# ==========Auth Section=========
# Used API from https://www.weatherapi.com/
api_key = ""

api_open = ""

account_sid = ""
auth_token = ""

# set up Twilio client
client = Client(account_sid, auth_token)



url_open = "https://api.openweathermap.org/data/2.5/forecast?" #openweather api
url_weatherapi = "https://api.weatherapi.com/v1//forecast.json" #weatherapi.com
weather_params = {
    "lat": 44.426765,
    "lon": 26.102537,
    "appid": api_open,
    "cnt": 4,
}

response = requests.get(url_open, params=weather_params)
response.raise_for_status()
json_data = response.json()
# print(json.dumps(json_data, indent=2))
# print(json_data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in json_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
    from_="+",
    body="Hello, It is going to rain today, Remember to bring an umbrella.",
    to='+'
    )
    print(message.status)
else:
    message = client.messages.create(
    from_="",
    body="Hello, Seems like there is no rain predicted for the next 12h ",
    to=''
    )
    print(message.status)