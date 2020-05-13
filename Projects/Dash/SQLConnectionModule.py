import pandas as pd
import pyodbc 
def connectSQLServer(driver, server, db, username, password):
    connSQLServer = pyodbc.connect(
        r'DRIVER={' + driver + '};'
        r'SERVER=' + server + ';'
        r'DATABASE=' + db + ';'
        r'UID=' + username + ';'
        r'PWD='+ password + ';',
        #r'Trusted_Connection=yes;',
        autocommit=True
    )
    return connSQLServer 

sql_conn = connectSQLServer(driver,server,db,username,password) cursor = sql_conn.cursor()
cursor.execute("""query""")
rows = cursor.fetchall()
dataSQL = []
for row in rows:
    dataSQL.append(list(row))
    labels = ['Dataframe Column Headers']
df = pd.DataFrame.from_records(dataSQL, columns=labels)
#print(df)
X = df['UserType']
Y = df['Status %']