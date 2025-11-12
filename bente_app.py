import mysql.connector

def get_cursor():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'ietsleuksdb'
    )

    cursor = conn.cursor()

    return conn, conn.cursor()

connection, cursor = get_cursor()
cursor.execute("""SELECT * FROM leukehobby""")

for row in cursor.fetchall():
    print(row)
connection.close()