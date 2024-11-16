'''
Project: Introduction to using SQL Development
Date: 11/11/2024
'''

# SQL = Structured Query Language, this is a way in which we can write commands to a database and store information:

# Importing a library, we are going to use the SQLite3 library:
import sqlite3 as sq

# Create a database and connect to this:
conn = sq.connect('firstDB.sql')

'''
We are going to create a table which stores employee details, example of the following:

ID | FN     | SN
1  | Fred   | Jones
2  | George | Jungle
3  | Jessica|Jones
'''

# This creates a cursor (c) to allow for interactions with the database: 
c = conn.cursor()

# SQL - How to create a table:
'''
Syntax:

CREATE TABLE IF NOT EXISTS tblName (
    col1 dataType validation,
    col2 dataType validation
);

'''

# Code to create our employees table:
# Primary Key = Unique Identifier
c.execute("""CREATE TABLE IF NOT EXISTS tblEmployees(
          ID integer PRIMARY KEY,
          FN text NOT NULL,
          SN text NOT NULL);""")

# View the data within our database table:
c.execute("""PRAGMA table_info(tblEmployees);""")
tableInfo = c.fetchall()
print(tableInfo)

# How to insert new data within our database table (tblEmployees):
'''
Syntax to insert data will look like this:

INSERT INTO tblName(col1, col2....) VALUES (val1, val2 ....);

Write a command that inserts this: 1  | Fred   | Jones
'''

# c.execute("""INSERT INTO tblEmployees(ID, FN, SN) VALUES("2", "George", "Jungle");""")

# # This will save the work to the database:
# conn.commit()

# Let's look to display some data from our database:
'''
Syntax for displaying data:
SELECT * FROM tblName;
* = Get every column
'''

# This will display all of the data within our employees table:
c.execute("""SELECT * FROM tblEmployees;""")
# To output the above, we run the below:
print(c.fetchall())

# Create a new table called tblJobs with the following with the following columns (JobID, JobName, Salary). Insert in three example rows and output these back out onto the screen.
# YOU ARE GOING TO NEED TO RESEARCH SQLite3 DATATYPES

# This will end the connection on our programme
conn.close()