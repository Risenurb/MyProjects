import requests
response = requests.get("http://127.0.0.1:8000/foodapi/1")
response_json = response.json()
print(response_json)
