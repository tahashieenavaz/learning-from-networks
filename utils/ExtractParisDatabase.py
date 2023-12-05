import mysql.connector

cnx = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="1200", database="metroparis")
cur = cnx.cursor()
cur.execute("SELECT * FROM connessione")
data = cur.fetchall()
print(data)
cnx.close()

