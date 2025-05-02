import sqlite3

db = sqlite3.connect("Cards.db")
cursor = db.cursor()
sql = "SELECT * from Card;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
