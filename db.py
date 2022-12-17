import sqlite3


class MyDataBase:
    banco = sqlite3.connect("system.db")
    cursor = banco.cursor()


    def __init__(self, banco=banco, cursor=cursor):
        self.banco = banco
        self.cursor = cursor


    def dailytable(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily (
            Id INTEGER PRIMARY KEY AUTOINCREMENT,
            cards INTEGER NOT NULL,
            dragon INTEGER NOT NULL,
            equips INTEGER NOT NULL,
            escort INTEGER NOT NULL,
            ruins INTEGER NOT NULL,
            pesca INTEGER NOT NULL,
            madeira INTEGER NOT NULL,
            minerio INTEGER NOT NULL
        )""")

        self.cursor.execute("""INSERT INTO daily (cards, dragon, equips, escort, ruins, pesca, madeira, minerio)
        VALUES (3, 2, 9, 1, 1, 40, 40, 40)""")  
        self.cursor.execute("""INSERT INTO daily (cards, dragon, equips, escort, ruins, pesca, madeira, minerio)
        VALUES (3, 2, 9, 1, 1, 40, 40, 40)""")  
        self.banco.commit()
        self.cursor.close()


    def send_default(self, defaultlist=[], farmlist=[]):
        self.cursor.execute("SELECT * FROM daily WHERE id = 2")
        data = self.cursor.fetchall()
        d = data[0]
        for each in d:
            if len(defaultlist) == 6:
                farmlist.append(each)
                if len(farmlist) == 3:
                    defaultlist.append(farmlist)
            else:
                defaultlist.append(each)
        self.cursor.close()
        return defaultlist

        
