import json

with open("user_bd.json", 'r') as file:
    data = json.load(file)
    print(data, type(data))
    file.close()
stuff = data + [{
    "Name": 1,
    "Class": 2,
    "xxx": 3
}]

with open("user_bd.json", 'w') as file:
    json_str = json.dump(stuff, file)
    file.close()
    print(json_str,"\n\n\n")

with open("user_bd.json", 'r') as file:
    data = json.load(file)
    print(data, type(data))
    file.close()