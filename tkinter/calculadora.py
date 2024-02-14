from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

Display = Entry(ventana) #ventana de entrada de texto
Display.grid(row=1, columnspan=6,sticky=W+E)


#Botones numericos
Button(ventana, text="1").grid(row=2,column=0,sticky=W+E)
Button(ventana, text="2").grid(row=2,column=1,sticky=W+E)
Button(ventana, text="3").grid(row=2, column=2,sticky=W+E)

Button(ventana, text="4").grid(row=3,column=0,sticky=W+E)
Button(ventana, text="5").grid(row=3,column=1,sticky=W+E)
Button(ventana, text="6").grid(row=3, column=2,sticky=W+E)

Button(ventana, text="7").grid(row=4,column=0,sticky=W+E)
Button(ventana, text="8").grid(row=4,column=1,sticky=W+E)
Button(ventana, text="9").grid(row=4, column=2,sticky=W+E)
Button(ventana, text="0").grid(row=5, column=1,sticky=W+E)


#Botones operacionales
'''
Button(ventana, text="AC").grid(row=5, column=0,sticky=W+E)
Button(ventana, text="%").grid(row=5, column=2,sticky=W+E)

Button(ventana, text= "-").grid(row=2,column=3, columnspan=2, sticky=W+E)
Button(ventana, text= "exp").grid(row=3, column=3, sticky=W+E)
Button(ventana, text= "2").grid(row=3,column=4, sticky=W+E)
Button(ventana, text= "(").grid(row=3,column=4, sticky=W+E)
#Button(ventana, text= ")").grid(row=4,column=4, sticky=W+E)
#Button(ventana, text= "=").grid(row=4,column=3, sticky=W+E)
'''

























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
