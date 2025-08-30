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

def init_find_player_for_id(idP):
    interaction_with_Json.person_search(idP)
    usefull.second_call_first_page()
    start_action()

def start_action():
    select = int(input("Select option: "))

    if select == 1:
        constants.console_cls()
        view_bd()
    elif select == 2:
        constants.console_cls()
        init_find_player_for_id(int(input("Enter id: ")))

    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
    elif select == 6:
        pass
    else:
        usefull.continue_enter_await("You're make a mistake, press Enter to continue")
        usefull.second_call_first_page()
