import os
from dotenv import load_dotenv
import json
import requests
from datetime import datetime

#loading \.env file
load_dotenv()

API_KEY = os.getenv('API_KEY')
USERNAME = os.getenv('USERNAME')
GRAPH = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":API_KEY,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# response_json = response.json()
# print(response_json)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH,
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

# update graph

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

today = datetime.now()

update_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

update = requests.post(url=update_endpoint, json=update_config, headers=headers)

print(update.text)

# PUT
data_to_edit = today.strftime("%Y%m%d")
edit_endpoint = f"{update_endpoint}/{data_to_edit}"

edit_params = {
    "quantity": "4"
}

edit = requests.put(url=update_endpoint, json=edit_params, headers=headers)
print(edit.text)