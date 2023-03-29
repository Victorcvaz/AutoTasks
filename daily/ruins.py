import pyautogui
from time import sleep
import routes


def ruins(runs):
    
    # Não executar a tarefa
    if runs == 0:
        print(f"{routes.time()} Pulamos Ruínas")
        return

    print(f"{routes.time()} Iniciando Ruínas")

    # Abrindo até o mapa atual
    routes.Maps.current_map()

    # Movendo até world maps
    routes.Maps.global_map()

    # Abrindo o mapa das ruínas
    routes.coordvalidation(x=1176, y=453)

    # Movendo até o spot
    routes.coordvalidation(x=1013, y=426)
    sleep(45)

    # Inicianto auto-ataque
    routes.Fight.auto_atk()

    # Membros auto-ataque
    routes.Fight.members_fight()

    # Aguardando completar a tarefa
    sleep(360)

    # Movendo até a recompensa
    routes.coordvalidation(x=91, y=257)
    routes.Fight.team_summon()
    sleep(20)

    # Fechando a tela de recompensa
    routes.coordvalidation(x=909, y=380)
    sleep(20)

    # Fechando a tela de informações

    
    print(f"{routes.time()} Terminamos Ruínas")