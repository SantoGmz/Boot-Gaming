import tkinter as tk
import time

ventana = tk.Tk()
ventana.title("Ejemplo label")


etiqueta = tk.Label(ventana, text="Hola son un label")
etiqueta.pack()

def actualizarHora():
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    etiqueta.after(1000, actualizarHora)#con after puedo actualizar cada cierto tiempo
    
    
actualizarHora()   
tk.mainloop()