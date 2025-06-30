import json

data = {"name": "kwanzu", "age": 20}
with open('test.json','w')as f:
   json.dump(data, f)

with open('test.json', 'r') as f:
    data = json.load(f)
    print(data)