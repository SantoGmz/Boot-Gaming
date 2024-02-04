import tkinter as tk


ventana = tk.Tk()
ventana.title("ejercicio 3")

boton = tk.Button(ventana, text="click me!")
boton.pack()


def botonPresionado():
    textoImp = tk.Label(ventana)
    textoImp.config(text=entrada.get())
    textoImp.pack()

    

entrada = tk.Entry(ventana)   
entrada.insert(0, "Nombre") 
entrada.pack()    
boton.config(command=botonPresionado)
ventana.mainloop()


#https://www.youtube.com/watch?v=Jl7ZByVMWrQ&list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ&index=3