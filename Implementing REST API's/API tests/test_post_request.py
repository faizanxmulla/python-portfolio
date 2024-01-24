import requests

base_url = "http://127.0.0.1:5000/book-reviews/post"
# base_url = "https://book-review-api-twy8.onrender.com/book-reviews/post"

body = {
    "book_title": "Moneywise",
    "author": "Deepak Shenoy",
    "rating": 7.9,
    "notes": "",
}

response = requests.post(base_url, json=body)
print(response.json(), response.status_code)
