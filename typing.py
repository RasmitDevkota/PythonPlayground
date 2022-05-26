import time
import pyautogui
import win32clipboard

letters = {
    "𝚊": "a",
    "𝚋": "b",
    "𝚌": "c",
    "𝚍": "d",
    "𝚎": "e",
    "𝚏": "f",
    "𝚐": "g",
    "𝚑": "h",
    "𝚒": "i",
    "𝚓": "j",
    "𝚔": "k",
    "𝚕": "l",
    "𝚖": "m",
    "𝚗": "n",
    "𝚘": "o",
    "𝚙": "p",
    "𝚚": "q",
    "𝚛": "r",
    "𝚜": "s",
    "𝚝": "t",
    "𝚞": "u",
    "𝚟": "v",
    "𝚠": "w",
    "𝚡": "x",
    "𝚢": "y",
    "𝚣": "z"
}

unicode_letters = [
    "U+1D68A",
    "U+1D68B",
    "U+1D68C",
    "U+1D68D",
    "U+1D68E",
    "U+1D68F",
    "U+1D690",
    "U+1D691",
    "U+1D692",
    "U+1D693",
    "U+1D694",
    "U+1D695",
    "U+1D696",
    "U+1D697",
    "U+1D698",
    "U+1D699",
    "U+1D69A",
    "U+1D69B",
    "U+1D69C",
    "U+1D69D",
    "U+1D69E",
    "U+1D69F",
    "U+1D6A0",
    "U+1D6A1",
    "U+1D6A2",
    "U+1D6A3"
]

mono = "𝚊 𝚋 𝚌 𝚍 𝚎 𝚏 𝚐 𝚑 𝚒 𝚓 𝚔 𝚕 𝚖 𝚗 𝚘 𝚙 𝚚 𝚛 𝚜 𝚝 𝚞 𝚟 𝚠 𝚡 𝚢 𝚣 \u2002".split(" ")
reg = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

time.sleep(3)

pyautogui.typewrite("$typing test")
pyautogui.hotkey("enter")

time.sleep(2.5)

pyautogui.tripleClick(384, 948)
pyautogui.hotkey("ctrl", "c")

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
test = data
win32clipboard.CloseClipboard()

print(test)

answer = ""

for l in range(len(test)):
    letter = test[l]

    answer += reg[mono.index(letter)]

pyautogui.click(744, 1054)
