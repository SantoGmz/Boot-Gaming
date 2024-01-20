
name= "Santos"
lastName= "Gomez"
legalAge = 18

try:

    age =  int(input("¿Que edad tienes?"))



    a = 1
    while age < legalAge:
        print("MIENTRAS SEAS MENOR DE EDAD NO PUEDES EJECUTAR ESTE CODIGO.")
        age =  int(input("¿Que edad tienes?"))
        if age > legalAge:
            print("YA ERES MAYOR DE EDAD!")
    else:
        print("ya pase el if.")
        

except Exception as e:
    print(f"Verificar lo siguiente -> {e}")








"""




try:
    print("Hola")
    if age > legalAge:
        print(f"eres mayor de {age} de edad!") 
    else:
        print(f"Lo sentimos, tu edad es:{age} y no es permitido aqui")

except Exception as ed:
    print(f"error {ed}")



_summary_
    

try:
    busco = pyautogui.locateOnScreen('fb-btn-option.png')
    if busco is not None:
        print("Se encontro en: ", busco)
    else:
        print("No se encontro")    
except  Exception as e:
    print(f"Error: {e}")
        """