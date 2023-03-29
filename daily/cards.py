import pyautogui
from time import sleep
import routes

def cards(runs):
    
    # Não executar a tarefa
    if runs == 0:
        print(f"{routes.time()} Pulamos cartas")
        return

    print(f"{routes.time()} Iniciando Cartas")

    # Movendo até reinos
    routes.Maps.kingdom_window()

    # Movendo até cartas
    routes.coordvalidation(x=760, y=473)

    # Movendo até go
    routes.Maps.go_button()
    sleep(20)

    for c in range(0,runs):

        # Movendo até Desafio
        routes.coordvalidation(x=737, y=678)
            
        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(120)
    
    # Abrindo tela de cartas pesadelo
    routes.coordvalidation(x=130, y=78)
    
    # Recolhedo recompensa de cartas pesadelo
    routes.coordvalidation(x=89, y=681)

    # removendo a tela de recompensa antes de clicar
    sleep(5)
    pyautogui.click()

    # Fechando a tela de cartas
    routes.coordvalidation(x=1300, y=55)
    
    # removendo a tela de recompensa antes de clicar
    routes.coordvalidation(x=282, y=735)

    print(f"{routes.time()} Terminamos Cartas")