import json
x={
    "name":"Arup",
    "age":19,
    "married":False,
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}
y=json.dumps(x,indent=4,separators=("  "," = "),sort_keys=True)
print(y)