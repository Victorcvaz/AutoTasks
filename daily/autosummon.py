import pyautogui
from time import sleep

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


def autosummon():
    """
        Módulo incompleto, estudar mais sobre como localizar imagens e usar os métodos.
    """
    # Abrindo a tela de atalhos
    pyautogui.moveTo(x=3712, y=655)
    sleep(2)
    pyautogui.click()

    # Abrindo o menu da guilda
    pyautogui.moveTo(x=3718, y=1927)
    sleep(2)
    pyautogui.click()
    
    # Movendo até a guilda
    pyautogui.moveTo(x=3003, y=1901)
    sleep(2)
    pyautogui.click()
    sleep(40)

    # Removendo o auto-ataque
    pyautogui.moveTo(x=2084, y=1735)
    sleep(2)
    pyautogui.click()

    # Inicianto fight dos membros do grupo
    pyautogui.moveTo(x=2410, y=1587)
    sleep(2)
    pyautogui.click()

    # Abrindo a mochila
    pyautogui.moveTo(x=2410, y=1587)
    sleep(2)
    pyautogui.click()

    

# Iniciando a summonar os sinos de fama

# pyautogui.locateOnScreen('freino.png')
x, y = pyautogui.locateCenterOnScreen('famareino.png', confidence=0.3)
pyautogui.moveTo(x, y)
#sleep(2)
#pyautogui.click()
#print()
print(x, y)

#.