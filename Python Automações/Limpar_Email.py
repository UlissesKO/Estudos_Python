import pyautogui
import time
import keyboard

pos1 = 437, 261
pos2 = 620, 261

while keyboard.is_pressed(' ') == False:
    pyautogui.leftClick(pos1, duration=0.2)
    pyautogui.leftClick(pos2, duration=0.2)
    time.sleep(2)
