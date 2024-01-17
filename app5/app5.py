import pyautogui
import time

time.sleep(1)  # Espera 5 segundos antes de buscar la imagen

#es bueno saber que si la imagen cambia de tamaño podria afectar el programa
try:
    boton2 = pyautogui.locateOnScreen('btn-2.png')
    if boton2 is not None:
        print("Botón encontrado en:", boton2)
    else:
        print("Botón no encontrado.")
except Exception as e:
    print(f"Error: {e}")