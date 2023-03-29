import pyautogui
from time import sleep
import routes

def tela_esquerda_superior(action='', count=''):

    
    if count == 1000:
        # Abrindo atalhos
        routes.coordvalidation(x=656, y=133)

        # Movendo até a fazenda
        routes.coordvalidation(x=621, y=178)
        return

    if action == 'Pesca':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=638, y=80) 
            
            # Movendo até a área de pesca
            routes.coordvalidation(x=338, y=223)

        else:

            # Iniciando a pesca 
            routes.coordvalidation(x=477, y=272, timer=False)  
        return

    if action == 'Madeira':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=639, y=81)

            # Movendo até a área de madeiras
            routes.coordvalidation(x=345, y=141)

        else:
            # Iniciando a colheta
            routes.coordvalidation(x=477, y=272, timer=False)     
        return

    if action == 'Minério':
        if count == 1001:
            
            # Abrindo maps
            routes.coordvalidation(x=638, y=79)

            # Movendo até a área de mineração
            routes.coordvalidation(x=371, y=100)

        else:
            # Iniciando a mineração
            routes.coordvalidation(x=477, y=272, timer=False)
        return


def tela_esquerda_inferior(action='', count=''):
    

    if count == 1000:
        # Abrindo a tela de atalhos
        routes.coordvalidation(x=658, y=518)

        # Movendo até a fazenda
        routes.coordvalidation(x=619, y=559)
        return

    if action == 'Pesca':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=640, y=462)
      
            # Movendo até a área de pesca
            routes.coordvalidation(x=338, y=607)

        else:
            # Iniciando a pesca
            routes.coordvalidation(x=475, y=654, timer=False)
        return

    if action == 'Madeira':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=640, y=462)

            # Movendo até a área de madeiras
            routes.coordvalidation(x=343, y=523)

        else:
            # Iniciando a colheta
            routes.coordvalidation(x=475, y=654, timer=False)    
        return

    if action == 'Minério':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=640, y=462)

            # Movendo até a área de mineração
            routes.coordvalidation(x=371, y=484)

        else:
            # Iniciando a mineração
            routes.coordvalidation(x=475, y=654, timer=False)
        return

             
def tela_direita_superior(action='', count=''):


    if count == 1000:
        # Abrindo a tela de atalhos
        routes.coordvalidation(x=1337, y=134)

        # Movendo até a fazenda
        routes.coordvalidation(x=1299, y=175)
        return
        
    if action == 'Pesca':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=1319, y=79)
            
            # Movendo até a área de pesca
            routes.coordvalidation(x=1018, y=222)

        else:
            # Iniciando a pesca
            routes.coordvalidation(x=1159, y=270, timer=False)   
        return

    if action == 'Madeira':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=1319, y=79)

            # Movendo até a área de madeiras
            routes.coordvalidation(x=1024, y=139)

        else:
            # Iniciando a colheta
            routes.coordvalidation(x=1159, y=270, timer=False)    
        return

    if action == 'Minério':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=1319, y=79)

            # Movendo até a área de mineração
            routes.coordvalidation(x=1052, y=100)

        else:
            # Iniciando a mineração
            routes.coordvalidation(x=1159, y=270, timer=False)
        return


def tela_direita_inferior(action='', count=''):
    

    if count == 1000:
        # Abrindo a tela de atalhos
        routes.coordvalidation(x=1337, y=519)

        # Movendo até a fazenda
        routes.coordvalidation(x=1300, y=562)
        return

    if action == 'Pesca':
        if count == 1001:
            # Abrindo maps
            routes.coordvalidation(x=1321, y=462)
            
            # Movendo até a área de pesca
            routes.coordvalidation(x=1018, y=607)

        else:
            # Iniciando a pesca
            routes.coordvalidation(x=1158, y=653, timer=False) 
        return

    if action == 'Madeira':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=1321, y=462)

            # Movendo até a área de madeiras
            routes.coordvalidation(x=1026, y=524)

        else:
            # Iniciando a colheta
            routes.coordvalidation(x=1158, y=653, timer=False)    
        return

    if action == 'Minério':
        if count == 1001:

            # Abrindo maps
            routes.coordvalidation(x=1321, y=462)

            # Movendo até a área de mineração
            routes.coordvalidation(x=1051, y=485)

        else:
            # Iniciando a mineração
            routes.coordvalidation(x=1158, y=653, timer=False)
        return


def changearea(window, place, area, runs=0):

      
    for start in range(place, 1002): 

        if window >= 1:
            if area == 'Pesca':
                if runs[0][0] == 0:
                    pass
                else:
                    tela_esquerda_superior(area, start)
            elif area == 'Madeira':
                if runs[0][1] == 0:
                    pass
                else:
                    tela_esquerda_superior(area, start)
            elif area == 'Minério':
                if runs[0][2] == 0:
                    pass
                else:
                    tela_esquerda_superior(area, start)
            else:
                tela_esquerda_superior(area, start)
        if window >= 2:
            if area == 'Pesca':
                if runs[1][0] == 0:
                    pass
                else:
                    tela_esquerda_inferior(area, start)
            elif area == 'Madeira':
                if runs[1][1] == 0:
                    pass
                else:
                    tela_esquerda_inferior(area, start)
            elif area == 'Minério':
                if runs[1][2] == 0:
                    pass
                else:
                    tela_esquerda_inferior(area, start)
            else:
                tela_esquerda_inferior(area, start)
        if window >= 3:
            if area == 'Pesca':
                if runs[2][0] == 0:
                    pass
                else:
                    tela_direita_superior(area, start)
            elif area == 'Madeira':
                if runs[2][1] == 0:
                    pass
                else:
                    tela_direita_superior(area, start)
            elif area == 'Minério':
                if runs[2][2] == 0:
                    pass
                else:
                    tela_direita_superior(area, start)
            else:
                tela_direita_superior(area, start)
        if window >= 4:
            if area == 'Pesca':
                if runs[3][0] == 0:
                    pass
                else:
                    tela_direita_inferior(area, start)
            elif area == 'Madeira':
                if runs[3][1] == 0:
                    pass
                else:
                    tela_direita_inferior(area, start)
            elif area == 'Minério':
                if runs[3][2] == 0:
                    pass
                else:
                    tela_direita_inferior(area, start)
            else:
                tela_direita_inferior(area, start)
        sleep(20)


def managefarm(runs, window):


    if window == 0 or runs == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]:
        return   

    if window == 1:
        autofarm_farm(runs[0])
    else:
        # Inicianto auto ataque individual dos membros(remover o seguir)
        routes.coordvalidation(x=418, y=287)

        # Movendo até a fazenda
        changearea(window, 1000, '')

        # Movendo até a área de pesca
        changearea(window, 1001, 'Pesca', runs)

        # Pesca
        for p in range(0, max(runs[0][0], runs[1][0], runs[2][0], runs[3][0])):
            if window >= 1:
                if p < runs[0][0]:
                    tela_esquerda_superior('Pesca')
            if window >= 2:
                if p < runs[1][0]:
                    tela_esquerda_inferior('Pesca')
            if window >= 3:
                if p < runs[2][0]:
                    tela_direita_superior('Pesca')
            if window >= 4:
                if p < runs[3][0]:
                    tela_direita_inferior('Pesca')
            sleep(10)
        # Madeira
        changearea(window, 1001, 'Madeira', runs)
        for f in range(0, max(runs[0][1], runs[1][1], runs[2][1], runs[3][1])):
            if window >= 1:
                if f < runs[0][1]:
                    tela_esquerda_superior('Madeira')
            if window >= 2:
                if f < runs[1][1]:
                    tela_esquerda_inferior('Madeira')
            if window >= 3:
                if f < runs[2][1]:
                    tela_direita_superior('Madeira')
            if window >= 4:
                if f < runs[3][1]:
                    tela_direita_inferior('Madeira')
            sleep(10)        
        # Minério
        changearea(window, 1001, 'Minério', runs)
        for u in range(0, max(runs[0][2], runs[1][2], runs[2][2], runs[3][2])):
            if window >= 1:
                if u < runs[0][2]:
                    tela_esquerda_superior('Minério')
            if window >= 2:
                if u < runs[1][2]:
                    tela_esquerda_inferior('Minério')
            if window >= 3:
                if u < runs[2][2]:
                    tela_direita_superior('Minério')
            if window >= 4:
                if u < runs[3][2]:
                    tela_direita_inferior('Minério')
            sleep(10)
        
        # Preparação para próximas instâncias (TELA SUPERIOR ESQUERDA)
        
        # Movendo a party para seguir o lider
        routes.coordvalidation(x=422, y=311)

        # Abrindo maps
        routes.coordvalidation(x=639, y=78)
        # World map
        routes.coordvalidation(x=195, y=76)
        # Laplace map
        routes.coordvalidation(x=268, y=149)
        # Laplace
        routes.coordvalidation(x=417, y=246)
        sleep(15)
        
        # FullScreen
        routes.coordvalidation(x=592, y=16)


def autofarm_farm(runslist):

    if runslist == [0 ,0, 0]:
        print(f"{routes.time()} Pulamos singlefarm")
        return
        
    print(f"{routes.time()} Iniciando Fazenda")

    # Abrindo a tela de atalhos
    routes.coordvalidation(x=1315, y=239)

    # Movendo até a fazenda
    routes.coordvalidation(x=1236, y=330)

    sleep(30)
    if runslist[0] != 0:
        # Abrindo maps
        routes.Maps.current_map()
        
        # Movendo até a área de pesca
        routes.coordvalidation(x=677, y=428)
        sleep(15)

        # Iniciando a pesca
        for c in range(0,runslist[0]):
            routes.coordvalidation(x=932, y=532)
            sleep(12)
        
        # Aguardando para ir até a próxima área
        sleep(18)

    if runslist[1] != 0:
        # Abrindo maps
        routes.Maps.current_map()

        # Movendo até a área de madeiras
        routes.coordvalidation(x=689, y=249)
        sleep(20)

        # Iniciando a colheta
        for c in range(0,runslist[1]):
            routes.coordvalidation(x=932, y=532)
            sleep(12)
        
        # Aguardando para ir até a próxima área
        sleep(15)

    if runslist[2] != 0:
        # Abrindo maps
        routes.Maps.current_map()

        # Movendo até a área de mineração
        routes.coordvalidation(x=749, y=167)
        sleep(20)

        # Iniciando a mineração
        for c in range(0,runslist[2]):
            routes.coordvalidation(x=932, y=532)
            sleep(12)
        
        # Aguardando próximo script
        sleep(12)
    
    print(f"{routes.time()} Terminamos Fazenda")