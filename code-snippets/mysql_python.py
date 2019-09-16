
""" importing 'mysql.connector' as mysql for convenient"""
import mysql.connector as mysql


""" connecting to the database using 'connect()' method
 it takes 3 required parameters 'host', 'user', 'passwd' """

"""
db = mysql.connect(
    host = "localhost",
    user = "shiva",
    passwd = "fhWoeN@1",
    auth_plugin='mysql_native_password'
)
print(db) # it will print a connection object if everything is fine

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## creating a databse called 'students'
## 'execute()' method is used to compile a 'SQL' statement
## below statement is used to create tha 'students' database
cursor.execute("CREATE DATABASE students")

## executing the statement using 'execute()' method
cursor.execute("SHOW DATABASES")

## 'fetchall()' method fetches all the rows from the last executed statement
databases = cursor.fetchall() ## it returns a list of all databases present

## printing the list of databases
print(databases)

## showing one by one database
for database in databases:
    print(database)
"""
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "fhWoeN@1",
    database = "students"
)

cursor = db.cursor()

## creating a table called 'users' in the 'students' database
# cursor.execute("CREATE TABLE users (id INT(10) NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20),food VARCHAR(30),confirmed CHAR(1),signup_date DATE)")

## getting all the tables which are present in 'students' database
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)

## 'DESC table_name' is used to get all columns information
cursor.execute("DESC users")

## it will print all the columns as 'tuples' in a list
print(cursor.fetchall())

## 'DROP TABLE table_name' statement will drop the table from a database
# cursor.execute("DROP TABLE users")

## dropping the 'id' column
# cursor.execute("ALTER TABLE users DROP id")

## adding 'email' column to the 'users' table
## 'FIRST' keyword in the statement will add a column in the starting of the table
# cursor.execute("ALTER TABLE users ADD COLUMN email VARCHAR(40) AFTER name")

"""Inserting entries into table"""
## defining the Query
query = "INSERT INTO users (id,name,email,food,confirmed,signup_date) VALUES (NULL, %s, %s,%s, %s, %s)"
## storing values in a variable
values = ("shiva", "shiva@gmail.com", "continental", "Y", "2019-08-31")

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")

"""Inserting multiple entries at a time"""

cursor = db.cursor()

## defining the Query
query = "INSERT INTO users (id,name,email,food,confirmed,signup_date) VALUES (NULL, %s, %s,%s, %s, %s)"
## storing values in a variable
values = [
    ("shiva1", "shiva1@gmail.com", "continental", "Y", "2019-08-31"),
    ("shiva2", "shiva2@gmail.com", "continental", "Y", "2019-08-31"),
    ("shiva3", "shiva3@gmail.com", "continental", "Y", "2019-08-31"),
    ("shiva4", "shiva4@gmail.com", "continental", "Y", "2019-08-31")
]

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "records inserted")

"""Getting all entries from table"""
## defining the Query
query = "SELECT * FROM users"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

""" Selecting only one column"""
## defining the Query
query = "SELECT name FROM users"

## getting 'user_name' column from the table
cursor.execute(query)

## fetching all usernames from the 'cursor' object
usernames = cursor.fetchall()

## Showing the data
for username in usernames:
    print(username)

""" Select multiple columns"""
## defining the Query
query = "SELECT name, email FROM users"

## getting 'name', 'user_name' columns from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
data = cursor.fetchall()

## Showing the data
for pair in data:
    print(pair)


""" Selecting a particular entry based on WHERE"""
## defining the Query
query = "SELECT * FROM users WHERE id = 3"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)


"""Sorting the result by using ORDER BY"""
## defining the Query
query = "SELECT * FROM users ORDER BY name"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

#### Descending order
## defining the Query
query = "SELECT * FROM users ORDER BY name DESC"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)

""" Deleting the entries"""
## defining the Query
query = "DELETE FROM users WHERE id = 3"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()

"""Updating the data"""
## defining the Query
query = "UPDATE users SET name = 'kumar' WHERE id = 1"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()
