import interaction_with_Json
import usefull


def get_ent(message): # возвращает ввод
    if message == None: return input()
    return input(f"{message}")

def view_bd():
    if interaction_with_Json.visualise_bd() == 0:pass
    else:
        usefull.second_call_first_page()
        start_action()

def start_action():
    select = int(input("Select option: "))

    if select == 1:
        view_bd()
    elif select == 2:
        pass
    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
    else: print("You're make a mistake")
