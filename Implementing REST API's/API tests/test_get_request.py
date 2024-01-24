import requests

# base_url = "http://127.0.0.1:5000/book-reviews"
base_url = "https://book-review-api-twy8.onrender.com/book-reviews"

params = {
    "sort": "DESC",
    "max_records": 3,
}

response = requests.get(base_url, params=params)
print(response.text)
