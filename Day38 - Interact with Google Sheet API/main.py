import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

ENDPOINT = 	"https://trackapi.nutritionix.com/v2/natural/exercise"



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
    "gener": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age_no
}


response = requests.post(url=ENDPOINT, json=params, headers=headers)
response.raise_for_status()
result = response.json()
print(result)