import os

def draw_menu(admin_name, options):
    #os.system("cls")
    draw_hat(admin_name)
    draw_cross_line_in_menu()
    draw_options(options)

def draw_cross_line_in_menu():#просто отделяющая линия
    pass

def draw_hat(admin_name):#здесь верхняя часть с информацие о меню админа
    print(f"Welcome to admin system, {admin_name}")

def draw_options(options):#Сюда должен передаваться список с доступными командами
    o_len = int(len(options))
    for i in range(o_len):
        print(options[i])