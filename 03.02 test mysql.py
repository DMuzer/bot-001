import pyodbc

driver = '{ODBC Driv}'
server = 'SERVER = dmuzer-test-sql-base.database.windows.net'
port = '1433'
db = 'dmuzer_sql_test_base'
user = 'UID =dmuzer'
pw = 'PWD=20e7T929032080'

conn_str = ';'.join([driver, server, port, db, user, pw])

conn_str = """
    Driver={SQL Server};
    Server=dmuzer-test-sql-base.database.windows.net,1433;
    Database=dmuzer_sql_test_base;
    Uid=dmuzer@dmuzer-test-sql-base;Pwd={20e7T929032080};
    Encrypt=yes;
    TrustServerCertificate=no;
    Connection Timeout=30;
"""
try :    
    conn = pyodbc.connect(conn_str)
except :
    print("Подключиться к БД не удалось")
    
cursor = conn.cursor()

cursor.execute("select * from main_table")

row = cursor.fetchone()
print(row)
rest_of_rows = cursor.fetchall()

print(len(rest_of_rows))
for row in rest_of_rows:
    print(row)