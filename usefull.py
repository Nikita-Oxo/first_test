import constants
import The_Visualizer

def second_call_first_page():
    constants.console_cls()
    The_Visualizer.draw_menu("Admin", constants.get_options())

def continue_enter_await(msgText):
    input(f"{msgText}")