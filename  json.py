import json


data = {

'name': 'Hermoine Granger',
'age': 28,
'City': 'East,London',
'Interests': ['Reading', 'Painting', 'Hiking'],
'is student': True


}
#Writing data into a json file
with open('data.json', 'w') as json_file:
          
    json.dump(data, json_file, indent=4)

print('Data has been written to data.json')


# Reading from the json file 
with open('data.json','r') as json_file:
#Load the json data from file
 loaded_data = json.load(json_file)

 print('data loaded from data.json')
 print(loaded_data)

 ##Modification to the json file created
 loaded_data['age'] = 32
 loaded_data['interests'].append ('Basketball, Shopping, Makeup')


 #Write modification to the file
with open('data.json','w') as json_file:
    json.dump(loaded_data, json_file, indent=4)

print('modified data to the data.json file')