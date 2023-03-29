from daily import equips, cards, dragon, escort, ruins, multifarm
import startconfig
import db
import pyautogui
from time import sleep


# Inicialização

while True:
    config = startconfig.initoptions()
    if config == 0:
        break
    elif config == 1:
        pass
    else:
        print(f"\033[1;33mInicializando\033m")
        sleep(4)

        # Alteração de tela(minimizando)
        pyautogui.moveTo(x=1182, y=19)
        sleep(2)
        pyautogui.click()

        # Instâncias
        # Ordem de execeução de tarefas   

        multifarm.managefarm(config[f"Fazenda com {config['Quantidade de contas para fazenda']} contas"], config["Quantidade de contas para fazenda"])

        cards.cards(config['Cartas'])

        dragon.dragon(config['Dragão'])
            
        equips.equips(config['Equipamentos'])

        ruins.ruins(config['Ruínas'])
            
        escort.escort(config['Escolta'])
        break
            
print(f"\033[1;34mEncerrando...\033[m")
    
