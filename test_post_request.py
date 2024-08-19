# test_post_request.py

import requests

# URL of the Flask endpoint
url = "http://0.0.0.0:8000/record"

# Data to be sent in the POST request
payload = {"engine_temperature": 0.3}

# Sending the POST request
response = requests.post(url, json=payload)

# Print the response from the server
print("Status Code:", response.status_code)
print("Response JSON:", response.json())