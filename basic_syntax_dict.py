users = {
    'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {
        'country': 'Malaysia',
        'street': 'Kulas Light',
        'city': 'Kuala Lumpur',
        'zipcode': '92998-3874',
        'geo': {
            'lat': '-37.3159',
            'lng': '81.1496'
            }
    }
}
print(users, '\n')
print(users['name'])
print(users['address']['country'])
print(users['address']['city'])
print(f"Latitude: {users['address']['geo']['lat']}")
print(f"Longitude: {users['address']['geo']['lng']}")
print(type(users))

print('\nChange dict to JSON')
print('The data type also changes from dict to str')
import json
result = json.dumps(users)
print(result)
print(type(result))

print('\nUsing json.dump, we can change the dict to create a new Json file')
with open('result.json', 'w') as file: #create a new file named "result", and write : "users" in it
    json.dump(users, file)

