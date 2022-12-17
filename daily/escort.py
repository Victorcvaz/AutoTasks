import pyautogui
from time import sleep
import routes

def escort(runs):
    
    # Não executar a tarefa
    if runs == 0:
        return

    # Movendo até reino
    routes.Maps.kingdom_window()

    # Movendo até escort
    sleep(5)
    pyautogui.moveTo(x=846, y=1385)
    sleep(3)
    pyautogui.click()

    # Movendo até go
    routes.Maps.go_button()
    sleep(50)

    # Iniciando a escolta
    sleep(5)
    pyautogui.moveTo(x=2697, y=1859)
    sleep(3)
    pyautogui.click()
    sleep(930)