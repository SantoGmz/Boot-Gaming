from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

Display = Entry(ventana)
Display.grid(row=1, columnspan=6,sticky=W+E)


#Botones
Button(ventana, text="1").grid(row=2,column=0)
Button(ventana, text="2").grid(row=2,column=1)
Button(ventana, text="3").grid(row=2, column=2)

Button(ventana, text="4").grid(row=3,column=0)
Button(ventana, text="5").grid(row=3,column=1)
Button(ventana, text="6").grid(row=3, column=2)

Button(ventana, text="7").grid(row=4,column=0)
Button(ventana, text="8").grid(row=4,column=1)
Button(ventana, text="9").grid(row=4, column=2)


























'''
Button(ventana, text="1").grid(row=2, column=0)
Button(ventana, text="2").grid(row=2, column=1)
Button(ventana, text="3").grid(row=2, column=2)

Button(ventana, text="4").grid(row=3, column=0)
Button(ventana, text="5").grid(row=3, column=1)
Button(ventana, text="6").grid(row=3, column=2)

Button(ventana, text="7").grid(row=4, column=0)
Button(ventana, text="8").grid(row=4, column=1)
Button(ventana, text="9").grid(row=4, column=2)

'''






ventana.mainloop()
