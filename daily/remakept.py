import pyautogui
from time import sleep


def cleanpt(nmembers):
    
    """
        A ordem dos membros deve sempre terminar com a conta interserver por último.
    """

    # Não executar a tarefa
    if nmembers == 0:
        return

    # Clicando na aba do time
    sleep(3)
    pyautogui.moveTo(x=500, y=450)
    sleep(3)
    pyautogui.click()
    
    for c in range(0,nmembers):

        # Movendo até o segundo membro da party
        sleep(3)
        pyautogui.moveTo(x=313, y=708)
        sleep(3)
        pyautogui.click()

        # Removendo membros do servidor
        if c < 3:
            sleep(3)
            pyautogui.moveTo(x=1082, y=1609)
            sleep(3)
            pyautogui.click()

        # Removendo membros inter-server
        else:
            sleep(3)
            pyautogui.moveTo(x=1070, y=1427)
            sleep(3)
            pyautogui.click()

        

    # Clicando em si mesmo na party
    sleep(3)
    pyautogui.moveTo(x=331, y=594)
    sleep(3)
    pyautogui.click()

    # Saindo do grupo
    sleep(3)
    pyautogui.moveTo(x=1052, y=938)
    sleep(3)
    pyautogui.click()

    # Confirmando
    sleep(3)
    pyautogui.moveTo(x=2355, y=1447)
    sleep(3)
    pyautogui.click()
    sleep(3)


def makept():
    """
       Workon it
    """
    # Movendo até o menu, abrindo o menu social
    pyautogui.moveTo()
    sleep(3)
    pyautogui.click

    # Clicando em contatos
    pyautogui.moveTo()
    sleep()
    pyautogui.click()

    # Abrindo o menu do membro