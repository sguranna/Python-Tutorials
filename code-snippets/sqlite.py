# import sqlite3

# dbase = sqlite3.connect('Our_data.db') # Open a database File
# print('Database opened')


# dbase.close()
# print( ' Database Closed')

""" Creating a table"""

# import sqlite3

# dbase = sqlite3.connect('my_data.db') # Open a database File
# print ('Database opened')

# dbase.execute(''' CREATE TABLE employee_records(
#      ID INT NOT NULL,
#      NAME TEXT NOT NULL,
#      COURSE TEXT NOT NULL,
#      MARKS INT NOT NULL) ''')

# print ('Table created')


# dbase.close()
# print (' Database Closed')

""" Adding contents/records"""

# import sqlite3

# dbase = sqlite3.connect('my_data.db') # Open a database File
# print ('Database opened')

# dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     DIVISION TEXT NOT NULL,
#     STARS INT NOT NULL) ''')

# print ('Table created')

# dbase.execute(''' INSERT INTO employee_records(ID,NAME,COURSE,MARKS)
#         VALUES(1,'James','EEE',98)
# ''')
# dbase.execute(''' INSERT INTO employee_records(ID,NAME,COURSE,MARKS)
#         VALUES(2,'Kumar','ECE',96)
# ''')
# dbase.commit()
# print ('REcord inserted')

# dbase.close()
# print (' Database Closed')

""" Adding data using functions"""
# import sqlite3

# dbase = sqlite3.connect('Our_data.db') # Open a database File
# print ('Database opened')

# dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     DIVISION TEXT NOT NULL,
#     STARS INT NOT NULL) ''')

# print ('Table created')

# def insert_record(ID,NAME,DIVISION,STARS):
#     dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
#             VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

#     dbase.commit()
#     print ('REcord inserted')
    
# insert_record(6,'Bob','Hardware',4)

# dbase.close()
# print (' Database Closed')

""" Reading data from table"""

# import sqlite3

# dbase = sqlite3.connect('my_data.db') # Open a database File
# print ('Database opened')

# dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     DIVISION TEXT NOT NULL,
#     STARS INT NOT NULL) ''')

# print ('Table created')

# def insert_record(ID,NAME,COURSE,STARS):
#     dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
#             VALUES(?,?,?,?)''',(ID,NAME,COURSE,MARKS))

#     dbase.commit()
#     print ('REcord inserted')
    
##insert_record(6,'Bob','Hardware',4)

# def read_Data():
#     # from math import *
#     data = dbase.execute(''' SELECT COURSE FROM employee_records''')
#     print(data)
#     for record in data:
#         print(record)
#         pass
#         # print ('ID : '+str(record[0]))
#         # print ('NAME : '+str(record[1]))
#         # print ('COURSE : '+str(record[2]))
#         # print ('MARKS : '+str(record[3])+'\n')


# read_Data()
# dbase.close()
# print (' Database Closed')

"""Updating a record"""

# # import sqlite3

# dbase = sqlite3.connect('my_data.db') # Open a database File
# print ('Database opened')

# # dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
# #     ID INT PRIMARY KEY NOT NULL,
# #     NAME TEXT NOT NULL,
# #     DIVISION TEXT NOT NULL,
# #     STARS INT NOT NULL) ''')

# # print ('Table created')

# # def insert_record(ID,NAME,DIVISION,STARS):
# #     dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
# #             VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

# #     dbase.commit()
# #     print ('REcord inserted')
    
# # ##insert_record(6,'Bob','Hardware',4)

# def read_Data():
#     # from math import *
#     print("sample")
#     data = dbase.execute(''' SELECT MARKS FROM employee_records''')
#     for record in data:
#         print(record)
#         # print ('ID : '+str(record[0]))
#         # print ('NAME : '+str(record[1]))
#         # print ('DIVISION : '+str(record[2]))
#         # print ('STARS : '+str(record[3])+'\n')


# # read_Data()


# def update_record():
#     dbase.execute(''' UPDATE employee_records set MARKS=90 WHERE ID=1 ''')
#     dbase.commit()
#     print ('Updated')

# update_record()
# print ('----------------------')
# read_Data()

# dbase.close()
# print (' Database Closed')

""" Deleting the records"""

# import sqlite3

# dbase = sqlite3.connect('my_data.db') # Open a database File
# print ('Database opened')

# dbase.execute(''' CREATE TABLE IF NOT EXISTS employee_records(
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     DIVISION TEXT NOT NULL,
#     STARS INT NOT NULL) ''')

# print ('Table created')

# def insert_record(ID,NAME,DIVISION,STARS):
#     dbase.execute(''' INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
#             VALUES(?,?,?,?)''',(ID,NAME,DIVISION,STARS))

#     dbase.commit()
#     print ('REcord inserted')
    
# ##insert_record(6,'Bob','Hardware',4)

# def read_Data():
#     # from math import *
#     data = dbase.execute(''' SELECT * FROM employee_records ORDER BY NAME''')
#     for record in data:
#         print ('ID : '+str(record[0]))
#         print ('NAME : '+str(record[1]))
#         print ('DIVISION : '+str(record[2]))
#         print ('STARS : '+str(record[3])+'\n')


# read_Data()


# def update_record():
#     dbase.execute(''' UPDATE employee_records set STARS=3 WHERE ID=2 ''')
#     dbase.commit()
#     print ('Updated')

# ##update_record()
# ##print ('----------------------')
# ##read_Data()


# def delete_record():
#     dbase.execute(''' DELETE from employee_records WHERE ID = 1 ''')
#     dbase.commit()
#     print ('Deleted')

# delete_record()
# print ('----------------------')
# # read_Data()

# dbase.close()
# print (' Database Closed')