import requests

base_url = "http://127.0.0.1:5000/book-reviews/delete"
# base_url = "https://book-review-api-twy8.onrender.com/book-reviews/delete"

book_title_to_delete = "uuu"

url = f"{base_url}?book_title={book_title_to_delete}"

response = requests.delete(url)
print(response.json(), response.status_code)
