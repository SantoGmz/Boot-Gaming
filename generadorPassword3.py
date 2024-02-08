import string #para generar tanto letras texto y digitos
import random #el nombre lo dice


abcedario = string.ascii_letters #variable para almacenar letras
numeros = string.digits #variable para almacenar Digitos numericos
simbbolosRaros = string.punctuation #variable para almacenar los raritos como: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
test= string.capwords #No se que carajos es esto

def generar_password(longitud): #esta funcion se encargar de crear la password
    caracteres = abcedario + numeros +simbbolosRaros #sirve para almacenar todo en una variable aunque puedo llamarlo desde aqui y simplificar mas e codigo lo dejare asi para entender cuando yo buela a leer esto
    password = "" #he tenido que creear la variable aqui porque no me dejaba crearla abajo
    for i in range(longitud): #el bucle dara vueltas por todos lados hasta los numeros que halla proporcionado el usuario
        password += random.choice(caracteres) #esta linea me dio demasiados problemas, aun no entiendo como lo resolvi pero lo importante es que funciona
    print(password)  
    
    
#hay que llamar la funcion y pasarle los valores          
generar_password(8)    