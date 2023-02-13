import time
from bot.pixel_search import get_coordinates
from bot.click_point import click


def main():
    while True:
        time.sleep(1)
        try:
            y, x = get_coordinates()
        except:
            continue
        click(x, y)


if __name__ == "__main__":
    main()
