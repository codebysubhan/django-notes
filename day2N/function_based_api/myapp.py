import requests, json
URL = "http://127.0.0.1:8000/studentapi/"

# READ
def get_student(id=None):
  data = {}
  if id != None:
      data['id'] = id
  json_data = json.dumps(data)
  headers = {'content-Type':'application/json'}
  r = requests.get(url=URL, headers=headers, data=json_data)
  result = r.json()
  print(result, type(result))
# POST
def post_data():
  data = {
      'name': 'farhan',
      'roll': 104,
      'city': 'karachi'
      }
  json_data = json.dumps(data)
  headers = {'content-Type':'application/json'}
  r = requests.post(url=URL, data=json_data, headers=headers)
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
  headers = {'content-Type': 'application/json'}
  r = requests.patch(url=URL, headers=headers, data=json_data)
  print(r.text, '----------------------------------------', r)
  data = r.json()
  print(data)
# DELETE
def delete_data():
  data = {
          'id': 3
          }
  json_data = json.dumps(data)
  headers = {'content-Type':'application/json'}
  r = requests.delete(url=URL, headers=headers, data=json_data)
  # print(r.text, '----------------------------------------')
  data = r.json()
  print(data)

# get_student()
# post_data()
update_data()
# delete_data()

