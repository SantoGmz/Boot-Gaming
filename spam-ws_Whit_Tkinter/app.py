import keyboard #importing the keyboard
import time #importing the mouse
import pyautogui #importing the boot
import tkinter as tk

ventana = tk.Tk()
ventana.title("WhatsApp Spammer by GmzSan")
ventana.geometry("350x350")

titulo1 = Label(ventana,text="xD")
titulo1.pack()

'''

2
2

while keyboard.is_pressed('q') == False:
   print("hola")
   time.sleep(1)
   
print("DONE!")   


i = 0

msg = input("Escribe el mensaje que quieres enviar: --> ")
numOfmsg = input("¿Cuantas veces sera enviado el mensaje?--> ")
print(f'el mensaje sera enviado {numOfmsg} veces')


time.sleep(3)
while keyboard.is_pressed('q') == False:
    
    while i < int(numOfmsg):
        pyautogui.typewrite(msg)
        pyautogui.press('Enter')
        time.sleep(0.3) 
        i = i+1
'''


tk.mainloop()        