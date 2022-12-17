import db

class DailyConfig:
    data = db.MyDataBase().send_default()

    def __init__(self, data=data):
        self.db_cards = data[1]
        self.db_dragon = data[2]
        self.db_equips = data[3]
        self.db_escort = data[4]
        self.db_ruins = data[5]
        self.db_farm = data[6]


    def config_cards(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_cards
        if option == 3:

            while True:
                try:
                    runs = str(input(
                        """Quantas repetições de cartas? 
                        \033[1;35m
                        [1] = 1x
                        [2] = 2x
                        [3] = 3x
                        [0] = Pular tarefa\033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) < 4:
                    print(f"Número informado: \033[1;35m{runs}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(runs)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_dragon(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_dragon
        if option == 3:

            while True:
                try:
                    runs = str(input(
                        """Quantas repetições de dragão? 
                        \033[1;35m
                        [1] = 1x
                        [2] = 2x
                        [0] = Pular tarefa\033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) < 3:
                    print(f"Número informado: \033[1;35m{runs}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(runs)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_equips(self, option):
        
        if option == 0:
            return 0
        if option == 1:
            return self.db_equips
        if option == 3:
            while True:
                try:
                    runs = str(input(
                        """Quantas repetições de equipamentos? 
                        \033[1;35m
                        [1] = 1x
                        [2] = 2x
                        [3] = 3x
                        [4] = 4x
                        [5] = 5x
                        [6] = 6x
                        [7] = 7x
                        [8] = 8x
                        [9] = 9x
                        [0] = Pular tarefa\033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) <= 9:
                    print(f"Número informado: \033[1;35m{runs}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(runs)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_escort(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_escort
        if option == 3:

            while True:
                try:
                    runs = str(input(
                        """Deseja executar escolta? 
                        \033[1;35m
                        [1] = Executar a tarefa
                        [0] = Pular tarefa
                        \033[m"""))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) < 2:
                    print(f"Número informado: \033[1;35m{runs}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(runs)
                print("\033[1;31mDigite um valor válido\033[m")

    def config_ruins(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_ruins
        if option == 3:

            while True:
                try:
                    runs = str(input(
                        """Deseja executar ruínas? 
                        \033[1;35m
                        1 = Executar a tarefa
                        0 = Pular tarefa
                        \033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) < 2:
                    print(f"Número informado: \033[1;35m{runs}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(runs)
                print("\033[1;31mDigite um valor válido\033[m")    


    def config_autofarm(self, option):
        
        if option == 0:
            return 0
        if option == 1:
            return self.db_farm
        if option == 3:
            farmlist = []
            while True:
                try:
                    runs = str(input(
                        """Deseja executar autofarm? 
                        \033[1;35m
                        1 = Executar no modo padrão
                        2 = Alterar tarefa
                        0 = Pular tarefa
                        \033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if runs.isnumeric() and int(runs) <= 2:
                    if int(runs) == 1:
                        return self.db_farm
                    if int(runs) == 0:
                        return 0
                    else:
                        break
            while True:
                    try:
                        pesca = str(input("Quantidade de turnos de pesca entre: [10,40] "))
                        madeira = str(input("Quantidade de turnos de madeira entre: [10,40] "))
                        minerio = str(input("Quantidade de turnos de minério [10,40] "))
                    except: 
                        print("Ocorreu algum erro, tente novamente")        
                    if pesca.isnumeric() and int(pesca) >= 10 and int(pesca) <= 40 and madeira.isnumeric() and int(madeira) >= 10 and int(madeira) <= 40 and minerio.isnumeric() and int(minerio) >= 10 and int(minerio) <= 40:
                        print(f"\033[1;32mOs valores digitados foram: Pesca {pesca}, Madeira {madeira}, Minério {minerio}\033[m")  
                        confirm = str(input("""
                        [Y] Confirmar 
                        [E] Editar
                        """))
                        if confirm.upper() == 'Y':
                            farmlist.append(int(pesca))
                            farmlist.append(int(madeira))
                            farmlist.append(int(minerio))
                            return farmlist
                    print("\033[1;31mOs valores não estão dentro dos parâmetros, tente novamente\033[m") 
                    print(f"\033[1;32mOs valores digitados foram: Pesca {pesca}, Madeira {madeira}, Minério {minerio}\033[m")  


