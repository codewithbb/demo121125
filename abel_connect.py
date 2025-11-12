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

def extract_rows_tabel(tabel_naam):
  myconn, mycursor = get_cursor()
  mycursor.execute(f"""SELECT * from {tabel_naam}""")
  rows = mycursor.fetchall()
  keys = [i[0] for i in mycursor.description]
  data = [dict(zip(keys, row)) for row in rows] ## dit is in json format
  return data






