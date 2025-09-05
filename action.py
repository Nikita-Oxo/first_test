import os

import interaction_with_Json
import usefull
import constants


def get_ent(message): # возвращает ввод
    if message == None: return input()
    return input(f"{message}")

def view_bd():
    interaction_with_Json.visualise_bd()
    usefull.second_call_first_page()
    start_action()

def init_find_player(param, for_what):
    interaction_with_Json.person_search(param, for_what)
    usefull.second_call_first_page()
    start_action()

def start_action():
    try:
        select = int(input("Select option: "))

        if select == 1:#Вывести Бд
            constants.console_cls()
            view_bd()
        elif select == 2:#Вывести инфо игрока по id
            constants.console_cls()
            init_find_player(int(input("Enter id: ")), "id")

        elif select == 3:#Добавить игрока
            constants.console_cls()
            #interaction_with_Json.add_player(str(input("Nikname: ")), int(input("Score: ")), int(input("level: ")))
            interaction_with_Json.init_add_new_player()
            usefull.second_call_first_page()
            start_action()

        elif select == 4:#Удалить игрока
            interaction_with_Json.delete_player(int(input("Enter id: ")))
            start_action()
        elif select == 5:#Поиск игрока по параметрам
            interaction_with_Json.init_find_for_parametrs()
            usefull.second_call_first_page()
            start_action()
        elif select == 6:#Закрыть программу
            os.close(1)
        else:
            usefull.continue_enter_await("You're make a mistake, press Enter to continue")
            usefull.second_call_first_page()
            start_action()
    except Exception as e:
        print(e)
        usefull.continue_enter_await("Something gone wrong, press Enter to continue")
        usefull.second_call_first_page()
        start_action()