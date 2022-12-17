import pyautogui
from time import sleep
import routes

def equips(runs):
    for c in range(0,runs):
        
        # Movendo até reinos
        routes.Maps.kingdom_window()

        # Movendo até equips
        sleep(5)
        pyautogui.moveTo(x=2387, y=858)
        sleep(3)
        pyautogui.click()

        # Movendo até go
        routes.Maps.go_button()
        if c == 0:
            sleep(30)

        # Movendo até o equips anterior após 3 iterações
        if c > 2 and c < 6:
            sleep(5)
            pyautogui.moveTo(x=961, y=1444)
            sleep(3)
            pyautogui.click()
        
        # Movendo até o equips anterior após 6 iterações
        if c > 5:
            sleep(5)
            pyautogui.moveTo(x=956, y=1107)
            sleep(3)
            pyautogui.click()
            
        # Movendo até o modo pesadelo
        sleep(5)
        pyautogui.moveTo(x=2524, y=1150)
        sleep(3)
        pyautogui.click()

        # Movendo até Desafio
        sleep(5)
        pyautogui.moveTo(x=2957, y=1916)
        sleep(3)
        pyautogui.click()

        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(170)
        

