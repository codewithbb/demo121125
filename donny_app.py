import mysql.connector

def get_cursor():
    myconn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ietsleuksdb'
    )

    return myconn, myconn.cursor()

def krijg_output(naam_tabel):
    connection, cursor = get_cursor()
    cursor.execute(f"SELECT * from {naam_tabel}")
    rows = cursor.fetchall()
    keys = [i[0] for i in cursor.description]
    data = [dict(zip(keys,row)) for row in rows]
    return data