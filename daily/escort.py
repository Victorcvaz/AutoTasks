import pyautogui
from time import sleep
import routes

def escort(runs):
    
    # Não executar a tarefa
    if runs == 0:
        print(f"{routes.time()} Pulamos Escolta")
        return
    
    print(f"{routes.time()} Iniciando Escolta")

    # Movendo até reino
    routes.Maps.kingdom_window()

    # Movendo até escort
    routes.coordvalidation(x=298, y=489)

    # Movendo até go
    routes.Maps.go_button()
    sleep(50)

    # Iniciando a escolta
    routes.coordvalidation(x=952, y=659)
    sleep(930)
    
    print(f"{routes.time()} Terminamos Escolta")