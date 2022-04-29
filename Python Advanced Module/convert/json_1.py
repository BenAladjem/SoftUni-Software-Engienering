import json
from random import randint
#a = [{"reportId":5201567,"deviceID":"863586031625605","timestamp":"2022-04-27T15:41:24+03:00","data":[{"higpsId":216,"value":"4","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":307,"value":"1","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":292,"value":"93","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":293,"value":"1110","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":294,"value":"74","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":295,"value":"1680","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":296,"value":"24.91","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":297,"value":"23.21","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":298,"value":"1335","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":299,"value":"3751","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":300,"value":"78","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":301,"value":"81","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":302,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":303,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":304,"value":"5","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":305,"value":"0","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":254,"value":"43.2258","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":255,"value":"27.84977","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":309,"value":"3","timestamp":"2022-04-27T15:41:24+03:00"},{"higpsId":258,"value":"","timestamp":"2022-04-27T15:41:24+03:00"}]}]


#j = b'U\xaa)\x03\x13 \xb0\xa9l\xb6\x01\x00\xd8\x01\x027\xa1\x00\xde\x02\x06**$$**\x00\xd2\x03\x08\xbc\x05\x12\x14?\x06\x12@\xcd\x04'

str_json = """{
  "response":{
    "count": 1234567,
    "items":[{
        "First name": "Tom",
        "ID": 123456,
        "Last name": "Krus"
    },{
        "First name": "Ben",
        "ID": 987654,
        "Last name": "Aladjem"
    }]    
}
}
"""

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'



#print(str_json)
#print(type(str_json))
data = json.loads(str_json)
#data = json.loads(x)
#print(data['response']['items'])
print(type(data))
for item in data['response']['items']:
    print(item['First name'], item['Last name'])
    #del item['First name']
    item['Likes'] = randint(50,100)
    print(item)

#new_json = json.dumps(data, indent = 2)
#print(new_json)
#print()
#print(json.loads(new_json))

#with open('my.json', 'w') as file:
 #   json.dump(data, file, indent=3)

with open('my.json', 'r') as file:
    data = json.load(file)
print(data)