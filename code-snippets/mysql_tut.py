""" importing 'mysql.connector' as mysql for convenient"""
import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "fhWoeN@1",
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
print(tables)
cursor.execute("DESC BASIC_DETAILS")
print(cursor.fetchall())
cursor.execute("SELECT * FROM BASIC_DETAILS")
print(cursor.fetchall())
query = "SELECT * FROM BASIC_DETAILS"
cursor.execute(query)
query = "INSERT INTO BASIC_DETAILS (SNO,Name,Age,Qual) VALUES (NULL, %s, %d,%s)"
values = [
    ("shiva1", 25, "BTech"),
    ("shiva2", 35, "MTech"),
    ("shiva3", 45, "MTech")
]

cursor.execute(query, values)
db.commit()

