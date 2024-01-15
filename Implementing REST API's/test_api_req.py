import requests

base_url = "https://book-review-api-twy8.onrender.com/text-processing"

params = {
    "text": "my name is ...   ",
    "duplication_factor": 4,
    "capitalization": "UPPER",
}

response = requests.get(base_url, params=params)

print(response.json(), response.status_code)
