import tkinter as tk

ventana = tk.Tk()



def firstClick(event):
    print("Diste Click")
    


boton1 = tk.Button(ventana, text="probar")

boton1.bind("<Button-2>", firstClick)

boton1.pack()
















ventana.mainloop()
