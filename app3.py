import pyautogui
#time la libreria para poder tomar segundos por momentos
import time

#hotkey es para las teclas que usare 
pyautogui.hotkey("win", "r")

time.sleep(1)
#write es para escribir lo que nesecite
pyautogui.write('brave.exe "google.com"', interval=0.2)

time.sleep(1)

#press es como lo dice, presionar dichas teclas
pyautogui.press("enter")