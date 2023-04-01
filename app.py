from utils.enumerators import Turn
from dialog_manager.DialogController import DialogController
from utils.io_utilities import *

controller = DialogController()


def main():
    # print("Loading Obi-1...")
    # loading_bar_anim()
    while True:
        output_text = controller.output_text()
        print_words(output_text, 0)
        user_input = ask_input()
        response = controller.elaborate_user_input(user_input)
        # if controller.scenario == Turn.QUESTION:
        #     three_dots_anim()
        print_words(f"{response}\n")

        if controller.proceed and controller.scenario == Turn.OUTRO:
            break


if __name__ == "__main__":
    main()
