from daily import equips, cards, dragon, escort, ruins, autofarm, remakept, andreza
import startconfig
import pyautogui
from time import sleep


# Inicialização
config = startconfig.initoptions()
print(config)
if config == 0:
    print(f"{startconfig.time()} \033[1;31mEncerrando...\033m")
    sleep(4)
else:
    print(f"{startconfig.time()} \033[1;33mInicializando\033m")
    sleep(4)
    
    # Alteração de tela
    pyautogui.keyDown('alt')
    pyautogui.press(['tab'])
    pyautogui.keyUp('alt')

    # Instâncias
    print(f"{startconfig.time()} Iniciando Cartas")
    cards.cards(config['cards'])
    print(f"{startconfig.time()} Terminamos Cartas")

    print(f"{startconfig.time()} Iniciando Dragão")
    dragon.dragon(config['dragon'])
    print(f"{startconfig.time()} Terminamos Dragão")

    print(f"{startconfig.time()} Iniciando Equipamentos")
    equips.equips(config['equips'])
    print(f"{startconfig.time()} Terminamos Equipamentos")

    print(f"{startconfig.time()} Iniciando Escolta")
    escort.escort(config['escort'])
    print(f"{startconfig.time()} Terminamos Escolta")

    print(f"{startconfig.time()} Iniciando Ruínas")
    ruins.ruins(config['ruins'])
    print(f"{startconfig.time()} Terminamos Ruínas")

    print(f"{startconfig.time()} Iniciando Fazenda")
    autofarm.autofarm_farm(config['autofarm'])
    print(f"{startconfig.time()} Terminamos Fazenda")

    # Gambiarra
    gambiarra = False
    if gambiarra:
        remakept.cleanpt(4)
        andreza.andrezafarm()
        autofarm.autofarm_farm(config['autofarm'])
        print(f"{startconfig.time()} Executamos a gambiarra")
    print(f"{startconfig.time()} \033[1;34mFim\033[m")
    