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

def moution_on_player(what, for_what, persone_info):

    try:
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):#проверка что такой элемент существует
            if data[item][f"{for_what}"] == persone_info:
                break

        if int(what) == 1:#Удалить аккаунт игрока
            new_list = []
            for i in range(len(data)):
                if data[i][f"{for_what}"] == persone_info:pass
                else:
                    new_list.append(data[i])

            with open("user_bd.json", 'w') as file:
                json.dump(new_list, file)
                file.close()

            usefull.continue_enter_await("All is good, press enter to continue.")
        elif int(what) == 2:#Изменить уровень игрока
            new_list = []
            for i in range(len(data)):
                if data[i][f"{for_what}"] == persone_info:
                    data[i]["level"] = input("Введите новый уровень: ")
                    new_list.append(data[i])
                else:
                    new_list.append(data[i])

            with open("user_bd.json", 'w') as file:
                json.dump(new_list, file)
                file.close()

            usefull.continue_enter_await("All is good, press enter to continue.")

        elif int(what) == 3:#Изменить счет игрока
            new_list = []
            for i in range(len(data)):
                if data[i][f"{for_what}"] == persone_info:
                    data[i]["score"] = input("Введите новый счёт: ")
                    new_list.append(data[i])
                else:
                    new_list.append(data[i])

            with open("user_bd.json", 'w') as file:
                json.dump(new_list, file)
                file.close()

            usefull.continue_enter_await("All is good, press enter to continue.")
        elif int(what) == 4:#Предупредить о неприемлемом нике
            usefull.continue_enter_await("Message has send to player, press Enter to continue")
        elif int(what) == 5:
            return "ex"
        else:
            usefull.continue_enter_await("You have a mistake, continue with Enter")

    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")


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

def person_search(param, for_what):
    try:
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):
            if for_what == "id":
                if data[item]["id"] == param:
                    while True:
                        constants.console_cls()
                        with open("user_bd.json", 'r') as file:#govnokod dl correct otobrajenia, kaus'
                            data = json.load(file)  # Data - list, data[0] - dict
                            file.close()
                        print(data[item])
                        draw_player_menu(constants.get_player_options())
                        if moution_on_player(int(input("Enter choose: ")), for_what, param) == "ex": return #что надо сделать с этим играком значение параметра по которому искали и параметр по которому искали
            # item это элемент {'id': 2, 'name': 'Newbie123', 'score': 300, 'level': 5, 'online': False} на котором находится игрок у которого айди совпадает с параметром
            # for_what это то, по чему мы ищем человека(например айди)
            # инт инпут это параметр what то что мы хотим сделать с игроком
            elif for_what == "NAME":pass
            elif for_what == "SCORE":pass
            elif for_what == "LEVEL":pass
            elif for_what == "ONLINE":pass
                #здесь появляется новое меню с действиями касаемо именно этого игрока
        #print("No information about player with that id")
        usefull.continue_enter_await("No information about player with that info")
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")



def init_add_new_player():
    try:
        name = str(input("enter Name: "))
        score = int(input("enter score: "))
        lvl = int(input("enter level: "))

        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()

        updatet_data = data+[{"id":int(len(data)+1),
                              "name": name,
                              "score": score,
                              "level": lvl,
                              "online": False}]
        with open("user_bd.json", 'w') as file:
            json.dump(updatet_data, file)
            file.close()
        usefull.continue_enter_await("All is good, press Enter to continue")
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")


def delete_player(id):
    try:
        new_list = []
        with open("user_bd.json", 'r') as file:
            data = json.load(file)#Data - list, data[0] - dict
            file.close()
        for item in range(len(data)):
            if data[item]["id"] == id:
                continue
            new_list.append(data[item])
        with open("user_bd.json", 'w') as file:
            json.dump(new_list, file)
            file.close()
        usefull.continue_enter_await("All is good, press Enter to continue")
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")