import keyboard #importing the keyboard
import time #importing the mouse
import pyautogui #importing the boot
from tkinter import *

ventana = Tk()
ventana.title("WhatsApp Spammer by GmzSan")
ventana.geometry("200x250")
ventana.resizable(False, False)#esto es para que no cambie el tamano nunca


def btn_click(msg):
    mensaje = msg.get()
    print(mensaje)
    


Label(ventana, text="Mensaje").grid(pady=0, padx=0, row=0, column=0)
Label(ventana, text="veces").grid(row=2,column=0)


msg = Entry(ventana, width=30).grid(padx=5, row=1, column=0)
numOfmsg = Entry(ventana, width=3).grid(row=3, column=0)

Button(ventana, text="iniciar", command=lambda: btn_click(msg), width=15).grid(row=4, column=0, pady=5)



































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


ventana.mainloop()        