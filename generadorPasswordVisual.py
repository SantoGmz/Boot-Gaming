import string #para generar tanto letras texto y digitos
import random #el nombre lo dice
import tkinter as tk


abcedario = string.ascii_letters #variable para almacenar letras
numeros = string.digits #variable para almacenar Digitos numericos
simbbolosRaros = string.punctuation #variable para almacenar los raritos como: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
test= string.capwords #No se que carajos es esto

def generar_password(longitud): #esta funcion se encargar de crear la password
    caracteres = abcedario + numeros +simbbolosRaros #sirve para almacenar todo en una variable aunque puedo llamarlo desde aqui y simplificar mas e codigo lo dejare asi para entender cuando yo buela a leer esto
    password = "" #he tenido que creear la variable aqui porque no me dejaba crearla abajo
    for i in range(longitud): #el bucle dara vueltas por todos lados hasta los numeros que halla proporcionado el usuario
        password += random.choice(caracteres) #esta linea me dio demasiados problemas, aun no entiendo como lo resolvi pero lo importante es que funciona
    return print(password)

    
    
#hay que llamar la funcion y pasarle los valores          
  


#longitud = input("De cuantos digitos quieres tu password?--> : ")

#generar_password(int(longitud))  

def imprime(event):
    generar_password(int(entrada.get())) #Aqui estoy llamando la funcion y llamando los datos del input y tambien convirtiendola en numero entero
    
    

#------------------------------------ Desde aquie estare programando lo grafico
#------------------------------------ From here is the GUI

ventana = tk.Tk()


passwordGUI = tk.Label(ventana, text="Te recomiendo usar: password")


textoPrincipal = tk.Label(ventana, text="Cuantos Digitos tendra tu password")
textoPrincipal.pack()


entrada = ""

#esto es el input    
entrada = tk.Entry(ventana)
entrada.pack()

#Esto es el boton crear
btn = tk.Button(ventana, text=("Crear"))


btn.bind("<Button-1>", imprime)



btn.pack()






















ventana.mainloop()