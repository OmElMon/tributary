import requests

# Define the URL of your Flask endpoint
url = "http://0.0.0.0:8000/record"

# Define the payload to send
payload = {"engine_temperature": 0.3}

# Send a POST request
response = requests.post(url, json=payload)

# Print the response from the server
print(response.json())