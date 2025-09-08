import The_Visualizer
import constants
import action


user_name = str(constants.get_admin_name())
constants.console_cls()

def firs_page():
    The_Visualizer.draw_menu(user_name, constants.get_options())
    action.start_action()

firs_page()

