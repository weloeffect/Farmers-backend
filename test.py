import requests

BASE_URL = "http://127.0.0.1:5000/"

res = requests.get(BASE_URL + "hello")
print('res', res.json())