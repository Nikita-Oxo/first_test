import json
import usefull
import constants
# with open("user_bd.json", 'r') as file:
#     data = json.load(file)
#     print(data, type(data))
#     file.close()
#
# print(data[0])
# print(type(data[0]))
# print(data[0]["id"])

def moution_on_player(what, id):
    if int(what) == 1:
        pass
    elif int(what) == 2:
        pass
    elif int(what) == 3:
        pass
    elif int(what) == 4:
        pass
    elif int(what) == 5:
        return "ex"

    else:
        usefull.continue_enter_await("You have a mistake, continue with Enter")



def visualise_bd():
    try:
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):
            print(f"{data[item]}")
        usefull.continue_enter_await("Press Enter to continue")
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")

def draw_player_menu(options):
    loptions = len(options)
    for i in range(loptions):
        print(options[i])

def person_search(find_persone_id):
    try:
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):
            if data[item]["id"] == find_persone_id:
                while True:
                    constants.console_cls()
                    print(data[item])
                    draw_player_menu(constants.get_player_options())
                    if moution_on_player(input("Enter choose: "), item) == "ex": return

                #здесь появляется новое меню с действиями касаемо именно этого игрока
        print("No information about player with that id")
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")
