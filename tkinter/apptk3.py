import tkinter as tk


ventana = tk.Tk()
ventana.title("ejercicio 3")

boton = tk.Button(ventana, text="click me!")
boton.pack()


def botonPresionado():
    texto = tk.Label(ventana, text="hola")
    texto.pack()
    
boton.config(command=botonPresionado)
ventana.mainloop()


#https://www.youtube.com/watch?v=Jl7ZByVMWrQ&list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ&index=3