import time
from random import uniform
from bot.pixel_search import get_coordinates
from bot.click_point import click


def main():
    while True:
        time.sleep(round(uniform(0.5, 1), 2))
        try:
            y, x = get_coordinates()
            click(x, y)
        except:
            continue


if __name__ == "__main__":
    main()
