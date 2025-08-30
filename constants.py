import os

def console_cls():
    os.system("cls")

def get_options():
    o = ["1. Вывести Бд",
         "2. Вывести инфо игрока по id",
         "3. Добавить игрока(todo)",
         "4. Удалить игрока(todo)",
         "5. Поиск игрока по параметрам(todo)",
         "6. Закрыть программу"]
    return o

def get_player_options():
    o = ["1. Удалить аккаунт игрока",
         "2. Изменить уровень игрока",
         "3. Изменить счет игрока",
         "4. Предупредить о неприемлемом нике",
         "5. Выйти из меню"]
    return o

def get_admin_name():
    return input("Hello, what's your name: ")
