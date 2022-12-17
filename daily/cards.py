import pyautogui
from time import sleep
import routes

def cards(runs):
    
    # Não executar a tarefa
    if runs == 0:
        return

    # Movendo até reinos
    routes.Maps.kingdom_window()

    # Movendo até cartas
    sleep(5)
    pyautogui.moveTo(x=2149, y=1321)
    sleep(3)
    pyautogui.click()

    # Movendo até go
    routes.Maps.go_button()
    sleep(20)

    for c in range(0,runs):

        # Movendo até Desafio
        sleep(5)
        pyautogui.moveTo(x=2064, y=1916)
        sleep(3)
        pyautogui.click()
            
        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(120)
    
    # Abrindo tela de cartas pesadelo
    sleep(5)
    pyautogui.moveTo(x=353, y=205)
    sleep(3)
    pyautogui.click()
    
    # Recolhedo recompensa de cartas pesadelo
    sleep(5)
    pyautogui.moveTo(x=259, y=1943)
    sleep(5)
    pyautogui.click()
    
    # removendo a tela de recompensa antes de clicar
    sleep(5)
    pyautogui.click()

    # Fechando a tela de cartas
    sleep(5)
    pyautogui.moveTo(x=3668, y=141)
    sleep(3)
    pyautogui.click()
    sleep(5)
    
    # removendo a tela de recompensa antes de clicar
    sleep(5)
    pyautogui.moveTo(x=259, y=1943)
    sleep(5)
    pyautogui.click()
