import mysql.connector

# Obtain connection string information from the portal

def get_cursor():
  myconn = mysql.connector.connect(
    host='localhost',
    user='abel',
    password='abel123',
    database='test_db',
    port="3307"
  )

  return myconn, myconn.cursor()

myconn, mycursor = get_cursor()
mycursor.execute("""SELECT * from test_tabel""")
rows = mycursor.fetchall()
print(rows)




