import time
from dialog_manager.DialogController import DialogController
from dialog_manager.DContextModel import DContextModel

controller = DialogController()
DContextModel = DContextModel()


def print_words(string):
    words = string.split()
    for i, word in enumerate(words):
        time.sleep(0.2)
        if i == 0:
            print(word, end="")
        else:
            print(" " + word, end="")


def main():
    while controller.proceed:
        output = controller.output_text()
        print_words(output)
        time.sleep(5000)


if __name__ == "__main__":
    main()
