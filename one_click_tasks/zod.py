import pyautogui
from time import sleep

pyautogui.keyDown('alt')
pyautogui.press(['tab'])
pyautogui.keyUp('alt')

# Movendo até maps
pyautogui.moveTo(x=3597, y=330)
sleep(1)
pyautogui.click()

# Movendo até world maps
pyautogui.moveTo(x=1048, y=299)
sleep(1)
pyautogui.click()

# Movendo até o map Sunflorest
pyautogui.moveTo(x=1879, y=1764)
sleep(1)
pyautogui.click()

# Movendo até Sunflorest zod
pyautogui.moveTo(x=2265, y=781)
sleep(1)
pyautogui.click()
sleep(50)
for c in range(0,8):
    # Abrindo aba de desafio
    pyautogui.moveTo(x=2347, y=1222)
    sleep(1)
    pyautogui.click()

    # Iniciando zod
    pyautogui.moveTo(x=2294, y=1286)
    sleep(1)
    pyautogui.click()

    # aguardando próxima run
    sleep(200)