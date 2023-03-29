# here we will make the class and methods to workon
import pyautogui
from time import sleep
from datetime import datetime

class Maps():


    def kingdom_window():

        # Movendo até a aba de reinos
        coordvalidation(x=1153, y=85)


    def go_button():

        # Clicando no botão de go
        coordvalidation(x=697, y=658)


    def forcar_entrada():

        # Forçar a entrada das instâncias
        sleep(3)
        coordvalidation(x=914, y=601)


    def current_map():

        # Abrindo o mapa atual
        coordvalidation(x=1280, y=122)


    def global_map():

        # Movendo até o mapa global
        coordvalidation(x=373, y=118)
    

class Fight():

    def auto_atk():

        # Inicianto auto-ataque do personagem
        coordvalidation(x=744, y=620)
    

    def members_fight():

        # Inicianto auto ataque individual dos membros
        coordvalidation(x=851, y=563)
    

    def team_summon():

        # Inicianto auto ataque individual dos membros
        coordvalidation(x=851, y=618)


def coordvalidation(x, y, timer=True):
    if timer:
        sleep(3)
    while True:
        pyautogui.moveTo(x=x, y=y)
        if str(pyautogui.position()) == str(f"Point(x={x}, y={y})"):
            pyautogui.click()
            break
    if timer:
        sleep(2)

def time():
    data = datetime.now()
    br_data_hora = data.strftime(f'\033[1;31m%d/%m/%Y %H:%M\033[m')

    return br_data_hora
