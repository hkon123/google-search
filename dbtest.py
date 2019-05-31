import pyodbc

connStr = (
    r"DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};"
    r"DBQ=C:\Users\hkonh\OneDrive\Dokumenter\hyperion.accdb;"
    )

conn = pyodbc.connect(connStr)
cursor = conn.cursor()
cursor.execute('select * from tblGoogle')

for row in cursor.fetchall():
    print (row)
