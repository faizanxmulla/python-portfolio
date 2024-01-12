import requests

base_url = "http://127.0.0.1:5000/text-processing"

params = {
    "text": "my name is ...   ",
    "duplication_factor": 4,
    "capitalization": "UPPER",
}

response = requests.get(base_url, params=params)

print(response.json(), response.status_code)
