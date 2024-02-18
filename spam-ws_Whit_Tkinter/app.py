'''
    Tuve que remover el evento de que confirma si hay una letra presionada como por ejemplo la q para   
    desactivar el programa.
    
'''

import tkinter as tk
import pyautogui
import time
from tkinter import PhotoImage

ventana = tk.Tk()
ventana.title("WhatsApp Spammer by GmzSan")
ventana.geometry("300x200")
ventana.resizable(False, False)

# Variable global para contar los mensajes enviados
i = 0

#la funcion
def on_click():
    global i
    msg = entrada.get()
    numOfmsg = entrada_num.get()  # Obtener el número de mensajes desde la entrada
    i = 0  # Reiniciar la variable i
    if not msg or not numOfmsg.isdigit(): # para confirmar si en algun lugar no hay digitos
        print("No tiene numeros")
    else:
        print("Escribiste -->", msg)
        print("Número de mensajes que se van a enviar -->", numOfmsg)
        time.sleep(3)
        while i < int(numOfmsg):
            pyautogui.typewrite(msg)
            pyautogui.press('Enter')
            time.sleep(0.3)
            i += 1
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\empieza el codigo de imagenes/////////////////////////////////////////

'''

///////////////////////////aqui la imagen////////////////////////////
try:
    def cargar_imagen(ruta):
        imagen = PhotoImage(file=ruta)
        return imagen


    # Cargar la imagen desde el archivo
    ruta_imagen = "bart.png"  # Reemplaza con la ruta de tu imagen
    imagen = cargar_imagen(ruta_imagen)

    # Crear un Label para mostrar la imagen
    label_imagen = tk.Label(ventana, image=imagen)
    label_imagen.pack()
except Exception as e:
    print(f"---> {e}")

'''


entrada = tk.Entry(ventana)
entrada.pack()


etiqueta_num = tk.Label(ventana, text="Número de mensajes a enviar:")
etiqueta_num.pack()

entrada_num = tk.Entry(ventana)
entrada_num.pack()

boton = tk.Button(text="Ejecutar", command=on_click)
boton.pack()

ventana.mainloop()
