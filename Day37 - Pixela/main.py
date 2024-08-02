import os
from dotenv import load_dotenv
import json
import requests

#loading \.env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAME')

pixela_endpoint = "https://pixe.la/v1/users"

print(API_KEY)
user_params = {
    "token":API_KEY,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# Create user
response = requests.post(url=pixela_endpoint, json=user_params, verify=False)
response_json = response.json()

is_success = response.json()

print(response.text)
print("===================")
print(response_json)
print("==============")
print(is_success)