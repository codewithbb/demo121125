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

def krijg_output():
    connection, cursor = get_cursor()
    cursor.execute("""SELECT * FROM leukehobby""")
    test = cursor.fetchall()
    for row in test:
        print(row)
    connection.close()

    return ("yes, het is gelukt! " + str(test))