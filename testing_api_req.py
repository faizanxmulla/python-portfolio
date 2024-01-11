import requests 

base_url = 'http://127.0.0.1:5000/text-processing'

params = {'text': 'my name is ...   '}

requests = requests.get(base_url, params=params)

print(requests.content, requests.json())