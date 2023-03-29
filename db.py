import sqlite3
from config import DailyConfig

class MyDataBase(DailyConfig):
    def __init__(self):
        self.banco = sqlite3.connect("system.db")
        self.cursor = self.banco.cursor()
    def standard_config(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS standard (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(30) NOT NULL UNIQUE,
            cards INTEGER NOT NULL,
            dragon INTEGER NOT NULL,
            equips INTEGER NOT NULL,
            escort INTEGER NOT NULL,
            ruins INTEGER NOT NULL,
            windows INTEGER NOT NULL,
            mfarmacc1pes INTEGER NOT NULL,
            mfarmacc1mad INTEGER NOT NULL,
            mfarmacc1min INTEGER NOT NULL,
            mfarmacc2pes INTEGER NOT NULL,
            mfarmacc2mad INTEGER NOT NULL,
            mfarmacc2min INTEGER NOT NULL,
            mfarmacc3pes INTEGER NOT NULL,
            mfarmacc3mad INTEGER NOT NULL,
            mfarmacc3min INTEGER NOT NULL,
            mfarmacc4pes INTEGER NOT NULL,
            mfarmacc4mad INTEGER NOT NULL,
            mfarmacc4min INTEGER NOT NULL)
            """)
        try:
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('default1' ,3 , 2, 9, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('default2' ,3 , 2, 6, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('default3' ,3 , 2, 0, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('Diárias com 9 equipamentos' ,3 , 2, 9, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('Diárias com 6 equipamentos' ,3 , 2, 6, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
            self.cursor.execute("""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, mfarmacc1pes, mfarmacc1mad, mfarmacc1min, mfarmacc2pes, mfarmacc2mad, mfarmacc2min, mfarmacc3pes, mfarmacc3mad, mfarmacc3min, mfarmacc4pes, mfarmacc4mad, mfarmacc4min)
            VALUES ('Diárias sem equipamentos' ,3 , 2, 0, 1, 0, 4, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40)""")
        except:
            pass
        self.banco.commit()
        self.cursor.close()

    
    def send_default(self, daily_id, defaultlist=[], farmlist=[], multilist=[]):
        self.cursor.execute(f"SELECT * FROM standard WHERE id = {daily_id}")
        data = self.cursor.fetchall()
        d = data[0]
        for each in d:
            if len(defaultlist) >= 8:
                farmlist.append(each)
                if len(farmlist) == 3:
                    multilist.append(farmlist)
                    farmlist = []
                    if len(multilist) == 4:
                        defaultlist.append(multilist)
            else:
                defaultlist.append(each)
        self.cursor.close()
        return defaultlist
    

    def select_daily_option_db(self, namelist=[]):
        self.cursor.execute(f"SELECT name FROM standard where id >= 4")
        data = self.cursor.fetchall()
        for d in data:
            namelist.append(d[0])
        data = DailyConfig.select_daily_option_config(namelist)
        self.cursor.close()
        return data
    

    def create_option_daily(self):
        data = DailyConfig.config_multifarm(3)
        data[0].join(',')
        [[404040], [0], [0, 0, 0], [0, 0, 0]]
        self.cursor.execute(f"""INSERT INTO standard (name, cards, dragon, equips, escort, ruins, windows, autofarm, mfarmacc1, mfarmacc2, mfarmacc3, mfarmacc4)
            VALUES ('default1' ,{DailyConfig.config_cards(3)} , {DailyConfig.config_dragon(3)}, {DailyConfig.config_equips(3)}, {DailyConfig.config_escort(3)}, {DailyConfig.config_ruins(3)}, {DailyConfig.config_windows(3)}, {DailyConfig.config_autofarm(3)}, {data[0]}, {data[1]}, {data[2]}, {data[3]})""")

MyDataBase().standard_config()