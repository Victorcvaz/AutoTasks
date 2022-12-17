# here we will make the class and methods to workon
import pyautogui
from time import sleep

class Maps():


    def kingdom_window():
        # Movendo até a aba de reinos
        
        sleep(5)
        pyautogui.moveTo(x=3260, y=207)
        sleep(3)
        pyautogui.click()


    def go_button():
        # Clicando no botão de go

        sleep(5)
        pyautogui.moveTo(x=1959, y=1871)
        sleep(3)
        pyautogui.click()


    def forcar_entrada():
        # Forçar a entrada das instâncias

        sleep(5)
        pyautogui.moveTo(x=2584, y=1694)
        sleep(5)
        pyautogui.click()


    def current_map():
        # Movendo até o mapa atual
        
        sleep(5)
        pyautogui.moveTo(x=3597, y=330)
        sleep(3)
        pyautogui.click()


    def global_map():
        # Movendo até o mapa global

        sleep(5)
        pyautogui.moveTo(x=1048, y=299)
        sleep(3)
        pyautogui.click()
    

class Fight():

    def auto_atk():
        # Inicianto auto-ataque do personagem
        sleep(3)
        pyautogui.moveTo(x=2084, y=1735)
        sleep(2)
        pyautogui.click()
    

    def members_fight():
        # Inicianto auto ataque individual dos membros
        sleep(3)
        pyautogui.moveTo(x=2410, y=1587)
        sleep(2)
        pyautogui.click()