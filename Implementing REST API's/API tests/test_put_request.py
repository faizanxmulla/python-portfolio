import requests

base_url = "http://127.0.0.1:5000/book-reviews/put"
# base_url = "https://book-review-api-twy8.onrender.com/book-reviews/put"

book_title_to_update = "Moneywise"

updated_body = {
    "author": "Deepak Shenoy",
    "rating": 7,
    "notes": "good book, but not for beginners.",
}

# including book title in the query parameters.
url = f"{base_url}?book_title={book_title_to_update}"

response = requests.put(url, json=updated_body)
print(response.json(), response.status_code)
