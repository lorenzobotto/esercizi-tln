import time
from dialog_manager.DialogController import DialogController
from dialog_manager.DContextModel import DContextModel

controller = DialogController()
DContextModel = DContextModel()


def ask_input(): return input("\n?- ")


def print_words(string, wait: float = 0):
    words = string.split()
    for i, word in enumerate(words):
        time.sleep(wait)
        print(word, end="") if i == 0 else print(f" {word}", end="")


def main():
    while controller.proceed:
        output = controller.output_text()
        print_words(output, 0)
        response = ask_input()


if __name__ == "__main__":
    main()
