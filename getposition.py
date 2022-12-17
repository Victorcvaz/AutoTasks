import pyautogui
print(pyautogui.position())

inicializacaolist = []
optionlist = [
            "[1] -   Cartas",
            "[2] -   Dragão",
            "[3] -   Equipamentos",
            "[4] -   Escolta",
            "[5] -   Ruínas",
            "[6] -   Autofarm",
            "[7] -   Cleanpt",
            "[0] -   Voltar ao menu"
            ]

for g in range(0, len(optionlist)-1):
    inicializacaolist.append(1)

for i in optionlist:
    print(i)
print(inicializacaolist)