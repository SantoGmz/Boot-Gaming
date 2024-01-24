from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#pip install keyboard para los eventos del teclado
#win32api, win32con - lei que era mas rapido que pyautogui en windows y linux




def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(528, 645) [0] == 0:
        click(528, 645)
    if pyautogui.pixel(332, 600) [0] == 0:
        click(414,600)            
    if pyautogui.pixel(332, 600) [0] == 0:
        click(520,600)
    if pyautogui.pixel(618, 663) [0] == 0:
        click(618, 663)            