import json 

#a python object(dict):
x={
    "name":"arup",
    "age":19,
    "city":"Siliguri"}
#convert into json
y=json.dumps(x) #json.dump() convert python to json

#the result in a JSON string:
print(y)