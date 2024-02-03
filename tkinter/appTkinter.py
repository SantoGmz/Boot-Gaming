from tkinter import *

window = Tk()
window.title("Primer Ventana")

entradaDeText = Entry(window)
entradaDeText.pack()


def firstClick():
    print(entradaDeText.get())#para imprimir lo que tiene le input tengo que ponerle el metodo .get()
    text = Label(window, text=entradaDeText.get())
    text.pack()

aButton = Button(window, text="click here!", command=firstClick) #command= se utiliza para llamar funciones y text es el nombre que llevara el boton
aButton.pack() #si no doy .pack() no se agrega a la ventana

window.mainloop() #mainloop() esto sirve para que el programa quede en un loop y no se cierre hasta que yo diga



