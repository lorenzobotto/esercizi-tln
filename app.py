import time

from dialog_manager.DialogController import DialogController
from dialog_manager.DContextModel import DContextModel

controller = DialogController()
DContextModel = DContextModel()


def main():
    while controller.proceed:
        controller.output_text()
        time.sleep(5000)


if __name__ == "__main__":
    main()
