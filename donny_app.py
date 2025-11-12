import mysql.connector

def get_cursor():
    myconn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ietsleuksdb'
    )

    return myconn, myconn.cursor()

connection, cursor = get_cursor()
cursor.execute("SELECT * FROM heel_leuk")
for row in cursor.fetchall():
    print(row)
connection.close()
