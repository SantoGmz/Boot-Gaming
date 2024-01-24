from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#pip install keyboard para los eventos del teclado
#win32api, win32con - lei que era mas rapido que pyautogui en windows y linux

# filas que nesecito
#X:  327 Y:  662 RGB: (168, 180, 227) f1
#X:  420 Y:  661 RGB: (171, 185, 226) f2
#X:  504 Y:  660 RGB: (174, 188, 229) f3
#X:  625 Y:  681 RGB: ( 54, 159, 198) f4


def click(x,y):
    
    pyautogui.click(x,y)
    """
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    """ 

    
while keyboard.is_pressed('q') == False:
    #f1
    if pyautogui.pixel(327, 662) [0] == 0:
        click(327, 662)
    #f2        
    if pyautogui.pixel(420, 661) [0] == 0:
        click(420, 661)        
    #f3            
    if pyautogui.pixel(504, 660) [0] == 0:
        click(504, 660)
    #f4        
    if pyautogui.pixel(625, 681) [0] == 0:
        click(625, 681)            