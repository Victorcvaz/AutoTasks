import pyautogui
from time import sleep
import routes


def ruins(runs):
    
    # Não executar a tarefa
    if runs == 0:
        return

    # Abrindo até o mapa atual
    routes.Maps.current_map()

    # Movendo até world maps
    routes.Maps.global_map()

    # Abrindo o mapa das ruínas
    sleep(5)
    pyautogui.moveTo(x=3296, y=1202)
    sleep(3)
    pyautogui.click()

    # Movendo até o spot
    sleep(5)
    pyautogui.moveTo(x=2618, y=864)
    sleep(3)
    pyautogui.click()
    sleep(45)

    # Inicianto auto-ataque
    routes.Fight.auto_atk()

    # Membros auto-ataque
    routes.Fight.members_fight()

    # Aguardando completar a tarefa
    sleep(360)

    # Movendo até a recompensa
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
