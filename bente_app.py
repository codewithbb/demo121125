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
    rows = cursor.fetchall()
    keys = [i[0] for i in cursor.description]
    data = [dict(zip(keys, row)) for row in rows]

    return (data)