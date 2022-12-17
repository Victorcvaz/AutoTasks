import pyautogui
from time import sleep
import routes

def autofarm_farm(runslist):

    if runslist == 0:
        return
        
    # Abrindo a tela de atalhos
    sleep(5)
    pyautogui.moveTo(x=3712, y=655)
    sleep(3)
    pyautogui.click()

    # Movendo até a fazenda
    sleep(5)
    pyautogui.moveTo(x=3496, y=913)
    sleep(3)
    pyautogui.click()
    sleep(30)

    # Abrindo maps
    routes.Maps.current_map()

    # Movendo até a área de pesca
    sleep(5)
    pyautogui.moveTo(x=1909, y=1198)
    sleep(3)
    pyautogui.click()
    sleep(15)

    # Iniciando a pesca
    for c in range(0,runslist[0]):
        pyautogui.moveTo(x=2604, y=1490)
        sleep(12)
        pyautogui.click()
    
    # Aguardando para ir até a próxima área
    sleep(12)

    # Abrindo maps
    routes.Maps.current_map()

    # Movendo até a área de madeiras
    sleep(5)
    pyautogui.moveTo(x=1950, y=714)
    sleep(3)
    pyautogui.click()
    sleep(20)

    # Iniciando a colheta
    for c in range(0,runslist[1]):
        pyautogui.moveTo(x=2628, y=1496)
        sleep(12)
        pyautogui.click()
    
    # Aguardando para ir até a próxima área
    sleep(12)

    # Abrindo maps
    routes.Maps.current_map()

    # Movendo até a área de mineração
    sleep(5)
    pyautogui.moveTo(x=2116, y=462)
    sleep(3)
    pyautogui.click()
    sleep(20)

    # Iniciando a mineração
    for c in range(0,runslist[2]):
        pyautogui.moveTo(x=2591, y=1487)
        sleep(12)
        pyautogui.click()
    
    # Aguardando próximo script
    sleep(12)
