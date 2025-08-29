import json

# with open("user_bd.json", 'r') as file:
#     data = json.load(file)
#     print(data, type(data))
#     file.close()
#
# print(data[0])
# print(type(data[0]))
# print(data[0]["id"])

def visualise_bd():
    try:
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):
            print(f"{data[item]}")
    except Exception as e:
        print(e)
        boof = input("Something gone wrong, enter some to continue")
        return 1

