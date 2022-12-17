from config import DailyConfig
from datetime import datetime

def initoptions(initdict={}, select=0):

        initlist = [
            "[1] - Iniciar com a configuração padrão",
            "[2] - Atualizar uma instância",
            "[3] - Atualizar todas as instâncias",
            "[4] - Iniciar apenas uma instância",
            "[5] - Atualizar o padrão de iniciação",
            "[0] - Encerrar o programa",
            ]
        
        configlist = [
            "[1] - Atualizar a configuração padrão",
            "[2] - Adicionar um nova nova iniciação",
            "[4] - Adicionar um nova nova iniciação",
            "[5] - Visualizar as opções de iniciação",
            "[0] - Voltar ao menu",
            ]
        
        optionlist = [
            "[1] -   Cartas",
            "[2] -   Dragão",
            "[3] -   Equipamentos",
            "[4] -   Escolta",
            "[5] -   Ruínas",
            "[6] -   Autofarm",
            "[0] -   Voltar ao menu",
            ]      

        while True:
            print()
            print(time())
            print()
            print(f"\033[1;35m{'Configurações':^40}\033[m")
            print()
            for p in initlist:
                print(f"\033[1;32m{p}\033[m")
            print()
            initoption = str(input("Selecione a sua opção: "))
            print()
            print()
            print()

            if initoption.isnumeric() and int(initoption) < len(initlist):      
                initoption = int(initoption)
                if initoption == 0:
                    return 0
                if initoption == 2 or initoption == 4:
                    while True:
                        print(time())
                        print()
                        for i in optionlist:
                            print(f"\033[1;32m{i}\033[m")
                        print()
                        print()
                        print()
                        select = str(input("Selecione a sua opção: "))
                        if select.isnumeric() and int(select) < len(optionlist):
                            select = int(select)
                            break
                        else:
                            print("\033[1;31mDigite um valor válido\033[m")
                # Voltar ao menu
                if initoption == 2 or initoption == 4:
                    if select == 0:
                        initoptions()
                
                # Configuração manual 
                # Atualize aqui quando for adicionado um novo optionlist 
                # Adicione a tarefa e replique as regras

                # Cartas task 1
                if initoption == 2 or initoption == 4:
                    if select == 1:
                        if initoption == 4:
                            initdict["cards"] = DailyConfig().config_cards(3)
                        else:
                            initdict["cards"] = DailyConfig().config_cards(3)
                    else:
                        if initoption == 4:
                            initdict["cards"] = DailyConfig().config_cards(0)
                        else:
                            initdict["cards"] = DailyConfig().config_cards(1)
                else:
                    initdict["cards"] = DailyConfig().config_cards(initoption)
                
                # Dragon task 2
                if initoption == 2 or initoption == 4:
                    if select == 2:
                        if initoption == 4:
                            initdict["dragon"] = DailyConfig().config_dragon(3)
                        else:
                            initdict["dragon"] = DailyConfig().config_dragon(3)
                    else:
                        if initoption == 4:
                            initdict["dragon"] = DailyConfig().config_dragon(0)
                        else:
                            initdict["dragon"] = DailyConfig().config_dragon(1)
                else:
                    initdict["dragon"] = DailyConfig().config_dragon(initoption)
                
                # Equipamentos task 3
                if initoption == 2 or initoption == 4:
                    if select == 3:
                        if initoption == 4:
                            initdict["equips"] = DailyConfig().config_equips(3)
                        else:
                            initdict["equips"] = DailyConfig().config_equips(3)
                    else:
                        if initoption == 4:
                            initdict["equips"] = DailyConfig().config_equips(0)
                        else:
                            initdict["equips"] = DailyConfig().config_equips(1)
                else:
                    initdict["equips"] = DailyConfig().config_equips(initoption)
                
                # Escolta task 4
                if initoption == 2 or initoption == 4:
                    if select == 4:
                        if initoption == 4:
                            initdict["escort"] = DailyConfig().config_escort(3)
                        else:
                            initdict["escort"] = DailyConfig().config_escort(3)
                    else:
                        if initoption == 4:
                            initdict["escort"] = DailyConfig().config_escort(0)
                        else:
                            initdict["escort"] = DailyConfig().config_escort(1)
                else:
                    initdict["escort"] = DailyConfig().config_escort(initoption)
                
                # Ruínas task 5
                if initoption == 2 or initoption == 4:
                    if select == 5:
                        if initoption == 4:
                            initdict["ruins"] = DailyConfig().config_ruins(3)
                        else:
                            initdict["ruins"] = DailyConfig().config_ruins(3)
                    else:
                        if initoption == 4:
                            initdict["ruins"] = DailyConfig().config_ruins(0)
                        else:
                            initdict["ruins"] = DailyConfig().config_ruins(1)
                else:
                    initdict["ruins"] = DailyConfig().config_ruins(initoption)
                
                # Autofarm task 6
                if initoption == 2 or initoption == 4:
                    if select == 6:
                        if initoption == 4:
                            initdict["autofarm"] = DailyConfig().config_autofarm(3)
                        else:
                            initdict["autofarm"] = DailyConfig().config_autofarm(3)
                    else:
                        if initoption == 4:
                            initdict["autofarm"] = DailyConfig().config_autofarm(0)
                        else:
                            initdict["autofarm"] = DailyConfig().config_autofarm(1)
                else:
                    initdict["autofarm"] = DailyConfig().config_autofarm(initoption)
                

                if initoption == 2 or initoption == 3 or initoption == 4:
                    print("\033[1;32mAlteração efetuada com sucesso\033[m")
                return initdict     
            else:
                print()
                print("\033[1;31mDigite um número válido\033[m")



def time():
    data = datetime.now()
    br_data_hora = data.strftime(f'\033[1;31m%d/%m/%Y %H:%M\033[m')

    return br_data_hora

