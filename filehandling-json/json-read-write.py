import json

with open('data.json') as f:
    data = json.load(f)

print(len(data))

for item in data:
    print(item['name'])

file = open('dump-1.json', 'w')

students = ('Alpha', 'Beta', 'Gamma')

file.write(json.dumps(students))

file = open('dump-2.json', 'w')

companies = ({"name":"Skriptx"}, { "name":"iSeed"})

file.write(json.dumps(companies))