import json.py


data={

'name': 'Hermoine Granger' 
'age': 27,
'City': 'East,London'
'Interests': ['Reading', 'Painting', 'Hiking']
'is student': True


}

with open('data.json', 'w') as json files:
          json.dump(data, json)