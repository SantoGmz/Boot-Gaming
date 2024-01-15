import pyautogui
import time

pyautogui.hotkey("win", "r")

time.sleep(1)
pyautogui.write('brave.exe "google.com"', interval=0.2)

time.sleep(1)


pyautogui.press("enter")