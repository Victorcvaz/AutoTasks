import pyautogui
from time import sleep
import routes

def equips(runs):

    if runs == 0:
        print(f"{routes.time()} Pulamos Equipamentos")
        return

    print(f"{routes.time()} Iniciando Equipamentos")

    for c in range(0,runs):
        
        # Movendo até reinos
        routes.Maps.kingdom_window()

        # Movendo até equips
        routes.coordvalidation(x=842, y=302)

        # Movendo até go
        routes.Maps.go_button()
        if c == 0:
            sleep(30)

        # Movendo até o equips anterior após 3 iterações
        if c > 2 and c < 6:
            routes.coordvalidation(x=355, y=517)
        
        # Movendo até o equips anterior após 6 iterações
        if c > 5:
            routes.coordvalidation(x=349, y=394)
            
        # Movendo até o modo pesadelo
        routes.coordvalidation(x=891, y=412)

        # Movendo até Desafio
        routes.coordvalidation(x=1036, y=676)

        # Movendo até forçar entrada
        routes.Maps.forcar_entrada()

        # Aguardando a próxima run
        sleep(170)
        
    print(f"{routes.time()} Terminamos Equipamentos")

