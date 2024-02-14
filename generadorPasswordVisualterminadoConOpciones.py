
import string
import random
import tkinter as tk

abecedario = string.ascii_letters
numeros = string.digits
simbolos_raros = string.punctuation

def generar_password(longitud, incluir_letras, incluir_numeros, incluir_simbolos):
    caracteres = ""
    if incluir_letras:
        caracteres += abecedario
    if incluir_numeros:
        caracteres += numeros
    if incluir_simbolos:
        caracteres += simbolos_raros

    if not caracteres:
        return "Selecciona al menos un tipo de caracter"

    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

def actualizar_etiqueta(text):
    label2.config(text=text)

def generar_y_mostrar_password():
    longitud = int(entrada.get())
    incluir_letras = var_letras.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    password = generar_password(longitud, incluir_letras, incluir_numeros, incluir_simbolos)
    actualizar_etiqueta(password)

ventana = tk.Tk()

passwordGUI = tk.Label(ventana, text="Te recomiendo usar: password")
passwordGUI.pack()

textoPrincipal = tk.Label(ventana, text="Cuantos Digitos tendra tu password")
textoPrincipal.pack()

entrada = tk.Entry(ventana)
entrada.pack()

# Variables para controlar los estados de los radio buttons
var_letras = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

# Crear radio buttons
chk_letras = tk.Checkbutton(ventana, text="Letras", variable=var_letras)
chk_numeros = tk.Checkbutton(ventana, text="Números", variable=var_numeros)
chk_simbolos = tk.Checkbutton(ventana, text="Símbolos", variable=var_simbolos)

chk_letras.pack()
chk_numeros.pack()
chk_simbolos.pack()

btn = tk.Button(ventana, text="Crear", command=generar_y_mostrar_password)
btn.pack()

label2 = tk.Label(ventana, text="")
label2.pack()

ventana.mainloop()