import pyautogui
from time import sleep
from .. import routes


pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')


# Movendo até reino
routes.Maps.kingdom_window()

# Movendo até arena
sleep(5)
pyautogui.moveTo(x=1465, y=883)
sleep(3)
pyautogui.click()

# Iniciando desafio
for c in range(0,5):
    sleep(5)
    pyautogui.moveTo(x=3102, y=634)
    sleep(3)
    pyautogui.click()
    # Inicianto auto-ataque
    sleep(3)
    routes.Fight.auto_atk()
    sleep(90)