from utils.enumerators import Turn
from speech.SpeechSynthesizer import SpeechSynthesizer
from speech.SpeechRecognitionHandler import SpeechRecognitionHandler
from dialog_manager.DialogController import DialogController
from utils.io_utilities import *

controller = DialogController(3)
speech_synth = None
speech_handler = None

if is_speech():
    speech_synth = SpeechSynthesizer()
    speech_handler = SpeechRecognitionHandler()


def main():
    # print("Loading Obi-1...")
    # loading_bar_anim()
    while True:
        initiative = controller.elaborate_initiative()
        print_words(initiative, wait=0.2, speech=speech_synth)
        if controller.done:
            break
        user_input = ask_input(handler=speech_handler)
        response = controller.elaborate_user_input(user_input)
        # if controller.turn == Turn.QUESTION:
        #     three_dots_anim()
        print_words(f"{response}\n", wait=0.4, speech=speech_synth)


if __name__ == "__main__":
    main()
