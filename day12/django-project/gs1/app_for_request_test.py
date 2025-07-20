import requests

URL = "http://127.0.0.1:8000/stuinfo/"

id = input('Enter id or leave empty:')
if id:
    URL = URL + id
r = requests.get(url = URL)

print(r.json())