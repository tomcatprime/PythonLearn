import requests

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token":"type your own token",
    "username": "jjj",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# Create user
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
