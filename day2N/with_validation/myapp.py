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
# def post_data():
#   data = {
#               'name': 'subhan',
#                       'roll': 104,
#                               'city': 'karahi'
#                                   }
#   json_data = json.dumps(data)
#   r = requests.post(url=URL, data=json_data)
#   print(r.text, '----------------------------------------')
#   data = r.json()
#   print(data)

def post_data():
    data = {
        'name': 'subhan',
        'roll': 104,
        'city': 'karachi'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)

    print(r.status_code)
    print(r.text, '----------------------------------------')

    try:
        data = r.json()
        print("Parsed JSON:", data)
    except json.JSONDecodeError:
        print("Non-JSON response:", r.text)

# UPDATE
def update_data():
  data = {
          'id': 6,
          'name': 'changed', # NOTE: roll is not given here
          'city': 'cityChanged'
      }
  json_data = json.dumps(data)
  r = requests.put(url=URL, data=json_data)
  # print(r.text, '----------------------------------------')
  data = r.json()
  print(data)
# DELETE
def delete_data():
  data = {
              'id': 7
                  }
  json_data = json.dumps(data)
  r = requests.delete(url=URL, data=json_data)
  # print(r.text, '----------------------------------------')
  data = r.json()
  print(data)




# get_student()
# post_data()
# update_data()
# delete_data()

