import pyautogui
from time import sleep
import routes as routes


pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


def apoc():
    # Movendo até reinos
    routes.Maps.kingdom_window()

    # Movendo e clicando na aba de apoc
    sleep(5)
    pyautogui.moveTo(x=3665, y=1322)
    sleep(3)
    pyautogui.click()

    # Movendo e clicando em go
    routes.Maps.go_button()
    sleep(50)

    # Iniciar desafio
    sleep(5)
    pyautogui.moveTo(x=2434, y=1946)
    sleep(3)
    pyautogui.click()

    # Movendo até forçar entrada e startando
    routes.Maps.forcar_entrada()
    