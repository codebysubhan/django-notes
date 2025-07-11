
import requests, json


URL = "http://127.0.0.1:8000/studentapi/"

def get_student(id=None):
    data = {}
    if id != None:
        data['id'] = id
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    result = r.json()
    print(result, type(result))

def create_student():
    data = {
        'name': 'abc',
        'roll': 104,
        'city': 'karahi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    # print(r.text, '----------------------------------------')
    data = r.json()
    print(data)


create_student()
# get_student(1)
