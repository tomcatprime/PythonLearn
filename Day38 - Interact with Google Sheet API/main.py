import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SHEETY_API = os.getenv('SHEETY_API')

ENDPOINT = 	"https://trackapi.nutritionix.com/v2/natural/exercise"



today = datetime.now()
formated_date = today.strftime("%d/%m/%Y")
formated_time = today.strftime("%H:%M")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}


exercise_text = input("Tell me what did you exercise: ")
gender = input("Your Gender: Male or Female? ")
weight_kg = int(input("Type your weight in kg: "))
height_cm = int(input("Type your height in cm: "))
age_no = int(input("Type your age: "))

params = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age_no
}


response = requests.post(url=ENDPOINT, json=params, headers=headers)
response.raise_for_status()
result = response.json()
exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

# Sheety API - update google sheet 

SHEEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_API}/myWorkouts/workouts"

# JSON payload

params_sheety = {
    "workout": {
        "date": formated_date,
        "time": formated_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
sheety_response = requests.post(url=SHEEETY_ENDPOINT, json=params_sheety, headers=sheety_headers)
sheety_response.raise_for_status()
status = sheety_response.status_code
if status == 200:
    print("Posted")
