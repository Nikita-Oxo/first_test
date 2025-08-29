import os

def console_cls():
    os.system("cls")

def get_options():
    o = ["1. Вывести Бд(todo)",
         "2. Вывести инфо игрока по id(todo)",
         "3. Добавить игрока(todo)",
         "4. Удалить игрока(todo)",
         "5. Поиск игрока по параметрам(todo)"]
    return o

def get_admin_name():
    return input("Hello, what's your name: ")
