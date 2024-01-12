import requests

base_url = "http://127.0.0.1:5000/uppercase"

params = {'text': 'my name is ...'}

response = requests.get(base_url, params=params)

print(response.json(), response.status_code)
