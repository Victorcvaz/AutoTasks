import pyautogui
from time import sleep


pyautogui.moveTo(x=3504, y=42)
sleep(2)
pyautogui.click()


def tela_esquerda_superior(count):

    if count == 0:
        # Abrindo o layout de match
        sleep(5)
        pyautogui.moveTo(x=1309, y=250)
        sleep(3)
        pyautogui.click()
    
    # Iniciando Match
    sleep(3)
    pyautogui.moveTo(x=1453, y=965)
    sleep(2)
    pyautogui.click()


def tela_esquerda_inferior(count):
    

    if count == 0:
        # Abrindo o layout de match
        sleep(5)
        pyautogui.moveTo(x=1297, y=1333)
        sleep(3)
        pyautogui.click()

    # Iniciando Match
    sleep(3)
    pyautogui.moveTo(x=1449, y=2037)
    sleep(2)
    pyautogui.click()        


def tela_direita_superior(count):

    if count == 0:
        # Abrindo o layout de match
        sleep(5)
        pyautogui.moveTo(x=3216, y=246)
        sleep(3)
        pyautogui.click()

    # Iniciando Match
    sleep(3)
    pyautogui.moveTo(x=3374, y=958)
    sleep(2)
    pyautogui.click()


def tela_direita_inferior(count):

    if count == 0:
        # Abrindo o layout de match
        sleep(5)
        pyautogui.moveTo(x=3223, y=1337)
        sleep(3)
        pyautogui.click()
    
    # Iniciando Match
    sleep(3)
    pyautogui.moveTo(x=3375, y=2039)
    sleep(2)
    pyautogui.click()

for c in range(0,200):
    tela_esquerda_superior(c)
    tela_esquerda_inferior(c)
    tela_direita_superior(c)
    tela_direita_inferior(c)
    sleep(60)