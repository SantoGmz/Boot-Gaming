#este script es para eliminar publicaciones de facebook
import pyautogui 
import time

time.sleep(3)


try:
    busco = pyautogui.locateOnScreen('fb-btn-option.png')
    if busco is not None:
        print("Se encontro en: ", busco)
    else:
        print("No se encontro")    
except  Exception as e:
    print(f"Error: {e}")
    
    
pyautogui.click('fb-btn-option.png')

    
    
    
    