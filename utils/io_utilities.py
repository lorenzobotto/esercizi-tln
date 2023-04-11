import re
import sys
import time
from threading import Thread
from speech.SpeechRecognitionHandler import SpeechException


def loading_bar_anim(time_interval: float = 0.01):
    bar_width = 20
    progress = 0
    block = '\u2588'
    empty = '\u2591'
    # loop through the progress bar
    while progress <= 100:
        percent_completed = progress / 100
        num_blocks = int(round(bar_width * percent_completed))
        num_empty = bar_width - num_blocks
        progress_bar = block * num_blocks + empty * num_empty

        sys.stdout.write('\r' + progress_bar + ' ' + str(progress) + '%')
        sys.stdout.flush()
        progress += 1

        time.sleep(time_interval)
    time.sleep(0.5)
    print("\n", flush=True)


def thread_dots(stop, info, time_interval: float = 0.5):
    while not stop():
        sys.stdout.write(info)
        sys.stdout.flush()
        i = 0
        time.sleep(time_interval)
        while i < 3:
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(time_interval)
            i += 1
        sys.stdout.write("\b" * (len(info) + 3))
        sys.stdout.flush()


def ask_input(handler):
    if handler:
        try:
            converted_text = handler.speak()
            print(converted_text)
            return converted_text
        except SpeechException as ex:
            print(ex)
            print("\n Let's try writing it... you can type your input now:")
    return input("\n?- ")


def print_words(string, wait: float = 0, speech=None):
    words = re.findall(r'\S+|\n', string)
    block = '\u2588'

    def _print(_string, _wait, _is_thread=False):
        time.sleep(3) if _is_thread else time.sleep(0)
        for i in range(len(words)):
            time.sleep(_wait)
            print(f"{words[i]} {block}", end="") if i == 0 or words[i - 1] == "\n" else \
                (print(f"\b\b {words[i]} {block}", end="") if words[i] != "\n" else print("\b \b", end="\n"))
            sys.stdout.flush()
        print("\b \b", end="\n")
        sys.stdout.flush()

    if speech:
        thread = Thread(target=_print, args=(string, 0.4, True))
        thread.start()
        speech.play(string)
        thread.join()
    else:
        _print(string, wait)


def is_speech():
    print("Do you want to use speech features to comunicate with Obi-1? (if this is the first run, a ~500MB model is "
          "going to be downloaded.)[y/n]")
    while True:
        ans = input("?-")
        match ans.lower():
            case "y":
                return True
            case "n":
                return False
            case _:
                print("Only y/n inputs are valid. Retry.")
