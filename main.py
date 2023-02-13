import time
from bot.pixel_search import get_coordinates
from bot.click_point import click


def main():
    while True:
        time.sleep(2)
        y, x = get_coordinates()
        click(x, y)


if __name__ == "__main__":
    main()
