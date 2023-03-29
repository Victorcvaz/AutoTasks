from config import DailyConfig
from db import MyDataBase
from time import sleep


def initoptions(initdict={}, select_one_daily=0):
    initdict.clear()
                # Opções
    initlist = [
        "[1] - Iniciar com a configuração padrão",
        "[2] - Inicialização personalizada",
        "[3] - Configurações",
        "[0] - Encerrar o programa",
        ]
    while True:
        print()
        print()
        print(f"\033[1;35m{'Inicialização':^{len(initlist[0])}}\033[m")
        print()
        for p in initlist:
            print(f"\033[1;32m{p}\033[m")
        print()
        initoption = str(input("Selecione a sua opção: "))
        print()
        print()
        print()
        if initoption.isnumeric() and int(initoption) < len(initlist):
            data = MyDataBase().send_default(daily_id=MyDataBase().select_daily_option_db())      
            initoption = int(initoption)
            if initoption == 0:
                # Encerrar
                return 0             
            elif initoption == 1:
                # Configuração manual, adicionar novas tarefas
                initdict['Nome'] = data[1]
                initdict["Cartas"] = DailyConfig(data).config_cards(1)
                initdict["Dragão"] = DailyConfig(data).config_dragon(1)
                initdict["Equipamentos"] = DailyConfig(data).config_equips(1)
                initdict["Escolta"] = DailyConfig(data).config_escort(1)
                initdict["Ruínas"] = DailyConfig(data).config_ruins(1)
                initdict["Quantidade de contas para fazenda"] = DailyConfig(data).config_windows(1)
                initdict[f"Fazenda com {initdict['Quantidade de contas para fazenda']} contas"] = DailyConfig(data).config_multifarm(1, initdict["Quantidade de contas para fazenda"])    

            elif initoption == 2:
                # Opções
                customlist = [
                    "[1] - Alterar uma instância",
                    "[2] - Iniciar apenas uma instância",
                    "[3] - Alterar todas as instâncias",
                    "[0] - Voltar ao menu",
                ]
                while True:
                    print()
                    print()
                    print(f"\033[1;32m{'Inicialização Personalizada':^{len(customlist[1])}}\033[m")
                    print()
                    for u in customlist:
                        print(f"\033[1;33m{u}\033[m")
                    print()
                    print()
                    print()
                    customselect = str(input("Selecione a sua opção: "))
                    if customselect.isnumeric() and int(customselect) < len(customlist):
                        customselect = int(customselect)
                        # Voltar ao Menu
                        if customselect == 0:
                            return 1
                        break
                    else:
                        print("\033[1;31mDigite um valor válido\033[m")
            
                if customselect == 3:
                    # Configuração manual, adicionar novas tarefas
                    initdict['Nome'] = f'Dados informados manualmente'
                    initdict["Cartas"] = DailyConfig(data).config_cards(3)
                    initdict["Dragão"] = DailyConfig(data).config_dragon(3)
                    initdict["Equipamentos"] = DailyConfig(data).config_equips(3)
                    initdict["Escolta"] = DailyConfig(data).config_escort(3)
                    initdict["Ruínas"] = DailyConfig(data).config_ruins(3)
                    initdict["Quantidade de contas para fazenda"] = DailyConfig(data).config_windows(3)
                    initdict[f"Fazenda com {initdict['Quantidade de contas para fazenda']} contas"] = DailyConfig(data).config_multifarm(3, initdict["Quantidade de contas para fazenda"])
                    
                elif customselect <= 2:
                    # Opções
                    optionlist = [
                    "[1] -   Cartas",
                    "[2] -   Dragão",
                    "[3] -   Equipamentos",
                    "[4] -   Escolta",
                    "[5] -   Ruínas",
                    "[6] -   Multifarm",
                    "[0] -   Voltar ao menu",
                    ]  
                    while True:
                        print()
                        for i in optionlist:
                            print(f"\033[1;36m{i}\033[m")
                        print()
                        print()
                        print()
                        select_one_daily = str(input("Selecione a sua opção: "))
                        if select_one_daily.isnumeric() and int(select_one_daily) < len(optionlist):
                            select_one_daily = int(select_one_daily)
                            break
                        else:
                            print("\033[1;31mDigite um valor válido\033[m")
                    # Voltar ao menu
                    if select_one_daily == 0: #configselect == 0
                        return 1
                    else:
                        # Configuração manual 
                        # Atualize aqui quando for adicionado um novo optionlist 
                        # Adicione a tarefa e replique as regras
                        initdict['Nome'] = f'{data[1]} + alteração manual'
                        # Cartas task 1
                        if select_one_daily == 1:
                            initdict["Cartas"] = DailyConfig(data).config_cards(3)
                        else:
                            if customselect == 2:
                                initdict["Cartas"] = DailyConfig(data).config_cards(0)
                            else:
                                initdict["Cartas"] = DailyConfig(data).config_cards(1)
                        
                        # Dragon task 2
                        if select_one_daily == 2:
                            initdict["Dragão"] = DailyConfig(data).config_dragon(3)
                        else:
                            if customselect == 2:
                                initdict["Dragão"] = DailyConfig(data).config_dragon(0)
                            else:
                                initdict["Dragão"] = DailyConfig(data).config_dragon(1)
                        
                        # Equipamentos task 3
                        if select_one_daily == 3:
                            initdict["Equipamentos"] = DailyConfig(data).config_equips(3)
                        else:
                            if customselect == 2:
                                initdict["Equipamentos"] = DailyConfig(data).config_equips(0)
                            else:
                                initdict["Equipamentos"] = DailyConfig(data).config_equips(1)
                        
                        # Escolta task 4
                        if select_one_daily == 4:
                                initdict["Escolta"] = DailyConfig(data).config_escort(3)
                        else:
                            if customselect == 2:
                                initdict["Escolta"] = DailyConfig(data).config_escort(0)
                            else:
                                initdict["Escolta"] = DailyConfig(data).config_escort(1)
                        
                        # Ruínas task 5
                        if select_one_daily == 5:
                            initdict["Ruínas"] = DailyConfig(data).config_ruins(3)
                        else:
                            if customselect == 2:
                                initdict["Ruínas"] = DailyConfig(data).config_ruins(0)
                            else:
                                initdict["Ruínas"] = DailyConfig(data).config_ruins(1)
                                
                        # Multifarm task 6
                        if select_one_daily == 6:
                            initdict["Quantidade de contas para fazenda"] = DailyConfig(data).config_windows(3)
                            initdict[f"Fazenda com {initdict['Quantidade de contas para fazenda']} contas"] = DailyConfig(data).config_multifarm(3, initdict["Quantidade de contas para fazenda"])
                        else:
                            if customselect == 2:
                                initdict["Quantidade de contas para fazenda"] = DailyConfig(data).config_windows(0)
                                initdict[f"Fazenda com {initdict['Quantidade de contas para fazenda']} contas"] = DailyConfig(data).config_multifarm(0, initdict["Quantidade de contas para fazenda"])
                            else:
                                initdict["Quantidade de contas para fazenda"] = DailyConfig(data).config_windows(1)
                                initdict[f"Fazenda com {initdict['Quantidade de contas para fazenda']} contas"] = DailyConfig(data).config_multifarm(1, initdict["Quantidade de contas para fazenda"])
            elif initoption == 3:
                # Trabalhando \/
                configlist = [
                    "[1] - Selecionar uma nova iniciação padrão",
                    "[2] - Adicionar um nova nova configuração de iniciação",
                    "[4] - Alterar o número de contas para farm de fazenda",
                    "[5] - Visualizar as opções de iniciação",
                    "[0] - Voltar ao menu",
                    ]
                # Trabalhando /\
                print("\033[1;31mEstamos trabalhando nessa opção, tente novamente mais tarde...\033[m")
                sleep(3)
                return 1
            return render_init_data(initdict)  
        else:
            print()
            print("\033[1;31mDigite um número válido...\033[m")
            sleep(3)


def render_init_data(current_data):
    print(f"\033[1;31m{current_data['Nome']}\033[m")
    print()
    for k, v in current_data.items():
        if v == 0 or v == [0, 0, 0] or v == [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]:
            print(f"{k}: Não será executado")
        elif k == 'Nome':
            pass
        else:
            print(f"{k}: {v}")
    print()
    while True:
            option = str(input(
                """\033[1;34mDeseja iniciar usando essas configurações?\033[m 
                \033[1;35m
                [1] = Iniciar
                [2] = Voltar ao menu
                [0] = Encerrar o programa\033[m
                """))      
            if option.isnumeric() and int(option) < 3:
                option = int(option)
                if option == 1:
                    return current_data
                if option == 2:
                    return 1
                if option == 0:
                    return 0
            print("\033[1;31mDigite um valor válido\033[m")
