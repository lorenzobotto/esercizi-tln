import re
import sys
import time
from threading import Thread


def loading_bar_anim(time_interval: float = 0.01):
    bar_width = 20
    progress = 0
    block = '▇'
    empty = '░'
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
        i = 0
        time.sleep(time_interval)
        while i < 3:
            sys.stdout.write(".")
            time.sleep(time_interval)
            i += 1
        sys.stdout.write("\b" * (len(info) + 3))


def ask_input(handler):
    if handler:
        handler.speak()
    return input("\n?- ")


def print_words(string, wait: float = 0, speech=None, ):
    words = re.findall(r'\S+|\n', string)

    def _print(_string, _wait):
        time.sleep(3)
        for i in range(len(words)):
            time.sleep(wait)
            print(words[i], end="") if i == 0 or words[i - 1] == "\n" else print(f" {words[i]}", end="")

    thread = Thread(target=_print, args=(string, wait,))
    thread.start()
    if speech:
        speech.play(string)
    thread.join()


def is_speech():
    print("Do you want to use speech features to comunicate with Obi-1? (if it's the first run, a ~500MB model is "
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
