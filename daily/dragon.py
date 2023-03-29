import pyautogui
from time import sleep
import routes


def dragon(runs):

    # Não executar a tarefa
    if runs == 0:
        print(f"{routes.time()} Pulamos Dragão")
        return

    print(f"{routes.time()} Iniciando Dragão")

    for c in range(0,runs):

        # Movendo até reinos
        routes.Maps.kingdom_window()

        # Movendo até dragon
        routes.coordvalidation(x=1087, y=388)

        # Movendo até go
        routes.Maps.go_button()
        if c == 0:
            sleep(20)

        # Movendo até Desafio
        routes.coordvalidation(x=865, y=666)

        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(145)  
            
    print(f"{routes.time()} Terminamos Dragão")