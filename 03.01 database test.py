import sqlite3

s = sqlite3.connect("dmuzer-test-sql-base.database.windows.net")

c = s.cursor()

tbl = c.execute(
                    """CREATE TABLE IF NOT EXISTS
                        MAIN_TABLE 
                        (ID, NAME, PHONE, LOGIN, PWD, EMAIL)""")

c.execute("""
            INSERT INTO
                MAIN_TABLE
            VALUES
                 ("00001", "Dmitry", "+7-916-724-82-54", "boss", "boss", "cpb.001@yandex.ru")
""")


tabls = c.execute(
    """
        SELECT  
            * 
        FROM MAIN_TABLE

""")
for row in tabls:
    print(row )