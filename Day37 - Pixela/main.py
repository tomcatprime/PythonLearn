import os
from dotenv import load_dotenv
import json
import requests

#loading \.env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAME')

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":API_KEY,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
<<<<<<< HEAD
# Create user
response = requests.post(url=pixela_endpoint, json=user_params, verify=False)
response_json = response.json()
=======
# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# response_json = response.json()
# print(response_json)
>>>>>>> 8a88bb2b01621a08d2dc2865fd88cdb945551219

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Study Python",
    "unit": "Commit",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": API_KEY
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

print(response.text)