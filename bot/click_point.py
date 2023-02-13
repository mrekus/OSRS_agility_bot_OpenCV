import win32api
import time
import pyautogui
from random import uniform


def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(round(uniform(0.1, 0.2), 2))
    pyautogui.click(clicks=1, interval=(round(uniform(0.1, 0.2), 2)))
