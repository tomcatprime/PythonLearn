import requests
import json
from datetime import datetime
MY_LAT = 48.2049
My_LNG = 16.3662

parameters = {
    "lat": MY_LAT,
    "lng": My_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
print(response.json())

print("######################################################")
data = response.json()

json_str = json.dumps(data, indent=4)
print(json_str)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)

time_now = datetime.now()
