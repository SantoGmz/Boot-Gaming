import keyboard #importing the keyboard
import time #importing the mouse
import pyautogui #importing the boot




'''

while keyboard.is_pressed('q') == False:
   print("hola")
   time.sleep(1)
   
print("DONE!")   


time.sleep(2)
pyautogui.typewrite("hello")
pyautogui.press('Enter')
'''
i = 0

msg = input("Escribe el mensaje: --> ")
numOfmsg = input("¿Cuantas veces sera enviado el mensaje?--> ")
print(f'el mensaje sera enviado {numOfmsg} veces')

time.sleep(3)
while i < int(numOfmsg):
    pyautogui.typewrite("hola")
    pyautogui.press('Enter')
    time.sleep(0.3) #si pongo menos de 0.3 se pone loco, no entiendo porque aun, REVISAR LUEGO.
    i = i+1
    