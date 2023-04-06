from utils.enumerators import Turn
from speech.SpeechSynthesizer import SpeechSynthesizer
from dialog_manager.DialogController import DialogController
from utils.io_utilities import *

controller = DialogController(3)
synth = SpeechSynthesizer() if is_speech() else None


def main():

    # print("Loading Obi-1...")
    # loading_bar_anim()
    while True:
        initiative = controller.elaborate_initiative()
        print_words(initiative, wait=0.2, speech=synth)
        if controller.done:
            break
        user_input = ask_input()
        response = controller.elaborate_user_input(user_input)
        # if controller.turn == Turn.QUESTION:
        #     three_dots_anim()
        print_words(f"{response}\n", wait=0.4, speech=synth)


if __name__ == "__main__":
    main()
