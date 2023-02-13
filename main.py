from bot.pixel_search import get_coordinates
from bot.click_point import click


def main():
    while True:
        coords = get_coordinates()
        click(coords)


if __name__ == "__main__":
    main()
