import re
import time
from dialog_manager.DialogController import DialogController

controller = DialogController()


def ask_input(): return input("\n?- ")


def print_words(string, wait: float = 0):
    words = re.findall(r'\S+|\n', string)
    for i in range(len(words)):
        time.sleep(wait)
        print(words[i], end="") if i == 0 or words[i - 1] == "\n" else print(f" {words[i]}", end="")


def main():
    while controller.proceed:
        output_text = controller.output_text()
        print_words(output_text, 0)
        user_input = ask_input()
        print_words(controller.elaborate_user_input(user_input)+"\n")


if __name__ == "__main__":
    main()
