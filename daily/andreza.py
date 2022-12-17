import pyautogui
from time import sleep


def andrezafarm():

# Trocando para a tela do personagem dela
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

# Movendo até a recompensa das ruínas
    sleep(5)
    pyautogui.moveTo(x=301, y=749)
    sleep(3)
    pyautogui.click()
    sleep(20)

    # Coletando a recompensa
    sleep(5)
    pyautogui.moveTo(x=3544, y=118)
    sleep(3)
    pyautogui.click()
    sleep(5)

