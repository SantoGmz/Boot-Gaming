import os
'''
#print("Comienza desde aqui")
print(os.getcwd()) #para saber donde estoy trabajjando
#print("hasta aqui")
os.getcwd
#os.mkdir("CarpetaPrueba2")#para crear carpeta
#os.remove("CarpetaPrueba")
print(os.getcwd)
#os.chdir("Desktop")#para moverme a diferente directorio
'''

def creaCArpeta(x):
    os.mkdir(x)

x = "carpetaZero"



comprobarCarpeta = os.path.exists(x)
if comprobarCarpeta == True:
    print("la carpeta existe")
else:
    creaCArpeta(x) 