import tkinter as tk
import keyboard
import pyautogui
import time

ventana = tk.Tk()
ventana.title("WhatsApp Spammer by GmzSan")
ventana.geometry("150x200")
ventana.resizable(False, False)#esto es para que no cambie el tamano nunca
#funciones
numOfmsg = 2

def on_click():
    nuevo = entrada.get()
    if not nuevo: #if not sirve para comprobar si tiene algun vacio
        print("no has escrito nada aun")
        
    else:
        print("Escribiste--> ", nuevo)
        time.sleep(3)
        while keyboard.is_pressed('q') == False:
            i=0
            while i < int(numOfmsg):
                pyautogui.typewrite(nuevo)
                pyautogui.press('Enter')
                time.sleep(0.3) 
                i = i+1
                



entrada = tk.Entry(ventana)
entrada.grid(column=0, row=1)
entrada.pack()



boton = tk.Button(text="ejecutar", command=on_click)
boton.pack()

























ventana.mainloop()        