import json
#some JSON:
x='{"name":"arup","age":19,"city":"Siliguri"}'
#parse x:
y=json.loads(x)

#the result in python dictionary:
print(y["age"])