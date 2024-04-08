import requests
import json
from datetime import datetime
MY_LAT = 48.2049
import smtplib

My_LNG = 16.3662

response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)

data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["latitude"])

def iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["latitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and My_LNG -5 <= iss_latitude <= My_LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": My_LNG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunset:
        return True
    
if iss() and is_night():
    connection = smtplib.SMTP()
    my_email = "email"
    my_password = "password"
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection = smtplib.SMTP("smtp-mail.outlook.com")

        connection.sendmail(from_addr=my_email, to_addrs="exampleemail@examlesmtp.com",
                            msg=f"Subject:Look UP, ISS!!!\n\n The ISS is above you in the sky.")
