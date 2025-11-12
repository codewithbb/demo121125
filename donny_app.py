import mysql.connector

def get_cursor():
    myconn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ietsleuksdb'
    )

    return myconn, myconn.cursor()

def krijg_output():
    connection, cursor = get_cursor()
    cursor.execute("SELECT * FROM heel_leuk")
    test = cursor.fetchall()
    for row in test:
        print(row)
    return "Dit is mijn output " + str(test)
    connection.close()