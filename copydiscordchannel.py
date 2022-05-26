import pyautogui
import time

time.sleep(3)

pyautogui.mouseDown(button='left')

for i in range(0, 5000):
    pyautogui.scroll(1000)

    time.sleep(0.0001)

pyautogui.mouseUp(button='left')