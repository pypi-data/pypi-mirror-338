import sys
import time
import shutil
from . import ascii_art, intro, subscribe

def scrolling_text(text, delay=0.05):
    width = shutil.get_terminal_size().columns
    padding = " " * width
    text = padding + text + padding

    for i in range(len(text) - width):
        sys.stdout.write("\r" + text[i: i + width])
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    for line in ascii_art.split("\n"):
        scrolling_text(line, delay=0.02)
    scrolling_text(intro, delay=0.02)

if __name__ == "__main__":
    main()
