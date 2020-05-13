import psycopg2
conn = psycopg2.connect(host=$host,database=$database, user=$user, password=$passwrd)
cursor = conn.cursor()
cursor.execute("""select * from information_schema.tables""")
rows = cursor.fetchall()
for row in rows:
    print(row)