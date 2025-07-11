import requests, json
URL = "http://127.0.0.1:8000/studentapi/"

# READ
def get_student(id=None):
    data = {}
    if id != None:
        data['id'] = id
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    result = r.json()
    print(result, type(result))
# POST
def post_data():
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
# UPDATE
def update_data():
    data = {
        'id': 3,
        'name': 'changed', # NOTE: roll is not given here
        'city': 'cityChanged'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    # print(r.text, '----------------------------------------')
    data = r.json()
    print(data)



# post_data()
# get_student()
update_data()