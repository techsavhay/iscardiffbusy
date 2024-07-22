import pyodbc 

server = 'DELL-LAPTOP'
database = 'iscardiffbusy'
username = 'sa'
password = 'SQLPa$$word'

# Establishing a connection to the SQL Server
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)

cursor = cnxn.cursor()

query = "SELECT * FROM events"

cursor.execute(query)


# Fetch one row at a time
#row = cursor.fetchone()
#while row:
#    print(row)
#    row = cursor.fetchone()

# Fetch all rows at once
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()