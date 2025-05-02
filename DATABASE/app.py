import sqlite3

db = sqlite3.connect("SQL_Practice_Assesment_Task7.db")
cursor = db.cursor()
sql = "SELECT * from Card;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()
