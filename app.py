from utils.enumerators import Turn
from dialog_manager.DialogController import DialogController
from utils.io_utilities import *

controller = DialogController(12)


def main():
    # print("Loading Obi-1...")
    # loading_bar_anim()
    while True:
        initiative = controller.elaborate_initiative()
        print_words(initiative, 0)
        if controller.done:
            break
        user_input = ask_input()
        response = controller.elaborate_user_input(user_input)
        # if controller.scenario == Turn.QUESTION:
        #     three_dots_anim()
        print_words(f"{response}\n")


if __name__ == "__main__":
    main()
