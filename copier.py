import pyautogui
import time

xi = 583
yi = 2
xf = 1337
yf = 1079

width = xf - xi
height = yf - yi

page_count = 2 + 18 + 822 + 4

images = []

print("initiating...")

time.sleep(3)

print("starting...")

for page in range(page_count):
    page_str = str(page).zfill(3)

    image = pyautogui.screenshot(region=(xi, yi, width, height))
    image.save("./stutzmanthiele/" + page_str + ".png")

    pyautogui.press("down")

    time.sleep(0.1)

print("done!")
