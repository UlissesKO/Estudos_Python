import pyautogui
import time

pos1 = 22, 110
pos2 = 109, 350

time.sleep(1)

while True:
    pyautogui.rightClick(pos1, duration=0.1)
    pyautogui.leftClick(pos2, duration=0.1)

