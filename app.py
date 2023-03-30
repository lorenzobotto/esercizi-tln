import time
from dialog_manager.DialogController import DialogController
from dialog_manager.DContextModel import DContextModel

controller = DialogController()
DContextModel = DContextModel()


def print_words(string, wait: float = 0):
    words = string.split()
    for i, word in enumerate(words):
        time.sleep(wait)
        if i == 0:
            print(word, end="")
        else:
            print(" " + word, end="")


def main():
    while controller.proceed:
        output = controller.output_text()
        print_words(output, 0)
        user_response = input("\nInput: ")
        print(user_response)


if __name__ == "__main__":
    main()
