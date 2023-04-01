import re
import sys
import time


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


def three_dots_anim(time_interval:float = 0.5):
    n = 2
    while n > 0:
        time.sleep(time_interval)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(time_interval)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(time_interval)
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(time_interval)
        sys.stdout.write('\b\b\b   \b\b\b')
        sys.stdout.flush()
        time.sleep(time_interval)
        n -= 1


def ask_input(): return input("\n?- ")


def print_words(string, wait: float = 0):
    words = re.findall(r'\S+|\n', string)
    for i in range(len(words)):
        time.sleep(wait)
        print(words[i], end="") if i == 0 or words[i - 1] == "\n" else print(f" {words[i]}", end="")
