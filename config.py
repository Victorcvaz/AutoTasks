class DailyConfig:
    def __init__(self, data):
        self.db_name = data[1]
        self.db_cards = data[2]
        self.db_dragon = data[3]
        self.db_equips = data[4]
        self.db_escort = data[5]
        self.db_ruins = data[6]
        self.db_windows = data[7]
        self.db_multifarm = data[8]


    def config_cards(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_cards
        if option == 3:

            while True:
                try:
                    daily = str(input(
                        """Configurações de cartas: 
                        \033[1;35m
                        [1] = 1x
                        [2] = 2x
                        [3] = 3x
                        [0] = Pular tarefa\033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if daily.isnumeric() and int(daily) < 4:
                    print(f"Número informado: \033[1;35m{daily}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(daily)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_dragon(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_dragon
        if option == 3:

            while True:
                try:
                    daily = str(input(
                        """Configurações de dragão: 
                        \033[1;35m
                        [1] = 1x
                        [2] = 2x
                        [0] = Pular tarefa\033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if daily.isnumeric() and int(daily) < 3:
                    print(f"Número informado: \033[1;35m{daily}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(daily)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_equips(self, option):
        
        if option == 0:
            return 0
        if option == 1:
            return self.db_equips
        if option == 3:
            while True:
                try:
                    daily = str(input(
                        """Configurações de equipamentos: 
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
                if daily.isnumeric() and int(daily) <= 9:
                    print(f"Número informado: \033[1;35m{daily}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(daily)
                print("\033[1;31mDigite um valor válido\033[m")


    def config_escort(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_escort
        if option == 3:

            while True:
                try:
                    daily = str(input(
                        """Configurações de escolta: 
                        \033[1;35m
                        [1] = Executar a tarefa
                        [0] = Pular tarefa
                        \033[m"""))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if daily.isnumeric() and int(daily) < 2:
                    print(f"Número informado: \033[1;35m{daily}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(daily)
                print("\033[1;31mDigite um valor válido\033[m")

    def config_ruins(self, option):

        if option == 0:
            return 0
        if option == 1:
            return self.db_ruins
        if option == 3:

            while True:
                try:
                    daily = str(input(
                        """Configurações de ruínas: 
                        \033[1;35m
                        1 = Executar a tarefa
                        0 = Pular tarefa
                        \033[m
                        """))
                except: 
                    print("Ocorreu algum erro, tente novamente")        
                if daily.isnumeric() and int(daily) < 2:
                    print(f"Número informado: \033[1;35m{daily}\033[m")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        return int(daily)
                print("\033[1;31mDigite um valor válido\033[m")    

    
    def config_windows(self, option):
        # função para configurar quantas telas serão usadas no multifarm
        if option == 0:
            return 0
        if option == 1:
            return self.db_windows
        if option == 3: 
            while True:
                print("Número de contas para coleta automática: ")
                windows = str(input("""\033[1;35m
                    1 = 1 conta
                    2 = 2 contas
                    3 = 3 contas
                    4 = 4 contas
                    0 = Cancelar
                        \033[m
                        """))
                if windows.isnumeric() and int(windows) >= 0 and int(windows) <= 4:
                    print(f"Quantidades de contas abertas simultaneamente: {windows}")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if confirm.upper() == 'Y':
                        if int(windows) == 0:
                            return 0
                        return int(windows)
                else:
                    print("\033[1;31mOcorreu algum erro, tente novamente.\033[m")
        

    def config_multifarm(self, option, windows):
        
        if windows == 0:
            return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if option == 1:
            return self.db_multifarm
        if option == 3 or option == 5:
            farmlist = []
    
            while True:
                daily = str(input(
                    """Configurações de fazenda com multiplas contas:
                    \033[1;35m
                    1 = Executar no modo padrão
                    2 = Alterar tarefa
                    0 = Não executar
                    \033[m
                    """))
                if daily.isnumeric() and int(daily) <= 2:
                    print(f"Opção selecionada: {daily}")
                    start = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    if start.upper() == 'Y':
                        pass
                    else:
                        if int(daily) == 1:
                            return self.db_multifarm
                        elif int(daily) == 0:
                            return [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
                        else:
                            break
                else:
                    print("Opção inválida!")
            for i in range(0, windows):
                while True:
                        pesca = str(input(f"Digite o valor de pesca da {i+1}º conta: [0,40] "))
                        madeira = str(input(f"Digite o valor de madeira da {i+1}º conta: [0,40] "))
                        minerio = str(input(f"Digite o valor de minério da {i+1}º conta: [0,40] "))     
                        if pesca.isnumeric() and int(pesca) >= 0 and int(pesca) <= 40 and madeira.isnumeric() and int(madeira) >= 0 and int(madeira) <= 40 and minerio.isnumeric() and int(minerio) >= 0 and int(minerio) <= 40:
                            print(f"\033[1;32mOs valores digitados foram: Pesca {pesca}, Madeira {madeira}, Minério {minerio}\033[m")  
                            confirm = str(input("""
                            [Y] Confirmar 
                            [E] Editar
                            """))
                            if confirm.upper() == 'Y':
                                farmlist.append([int(pesca), int(madeira), int(minerio)])
                                break
                        else:        
                            print("\033[1;31mOs valores não estão dentro dos parâmetros, tente novamente\033[m") 
                            print(f"\033[1;32mOs valores digitados foram: Pesca {pesca}, Madeira {madeira}, Minério {minerio}\033[m")  
            if windows == 1:
                farmlist.append([0 , 0, 0])
                farmlist.append([0 , 0, 0])
                farmlist.append([0 , 0, 0])
                return farmlist
            if windows == 2:
                farmlist.append([0 , 0, 0])
                farmlist.append([0 , 0, 0])
                return farmlist
            if windows == 3:
                farmlist.append([0 , 0, 0])
                return farmlist
            if windows == 4:
                return farmlist
    

    def select_daily_option_config(option_names):
        while True:
            count=1
            print(f"\033[1;32m{'Opções':^{len(option_names[0])}}\033[m")
            print()
            for n in option_names:
                print(f"\033[1;35m{count} = {n}\033[m")
                count+=1
            print()
            daily = str(input("Selecione a configuração de diárias "))
            if daily.isnumeric() and int(daily) <= len(option_names):
                    print(f"Opção selecionada: {daily}")
                    confirm = str(input("""
                    [Y] Confirmar 
                    [E] Editar
                    """))
                    print()
                    if confirm.upper() == 'Y':
                        break
        return int(daily)+3

