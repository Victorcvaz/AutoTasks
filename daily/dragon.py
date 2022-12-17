import pyautogui
from time import sleep
import routes


def dragon(runs):

    # Não executar a tarfe
    if runs == 0:
        return
    
    for c in range(0,runs):

        # Movendo até reinos
        routes.Maps.kingdom_window()

        # Movendo até dragon
        sleep(5)
        pyautogui.moveTo(x=3094, y=1070)
        sleep(3)
        pyautogui.click()

        # Movendo até go
        routes.Maps.go_button()
        if c == 0:
            sleep(20)

        # Movendo até Desafio
        sleep(5)
        pyautogui.moveTo(x=2437, y=1869)
        sleep(3)
        pyautogui.click()

        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(130)      