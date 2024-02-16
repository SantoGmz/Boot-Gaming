import tkinter as tk

ventana = tk.Tk()
ventana.title("WhatsApp Spammer by GmzSan")
ventana.geometry("150x200")
ventana.resizable(False, False)#esto es para que no cambie el tamano nunca
#funciones
def on_click():
    nuevo = entrada.get()

    print("Escribiste--> ", nuevo)



entrada = tk.Entry(ventana)
entrada.grid(column=0, row=1)
entrada.pack()



boton = tk.Button(text="ejecutar", command=on_click)
boton.pack()

























ventana.mainloop()        