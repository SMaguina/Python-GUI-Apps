import sqlite3

conn = sqlite3.connect('simpsons.db')

# create table named SIMPSON_INFO
conn.execute("CREATE TABLE SIMPSON_INFO( ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, GENDER TEXT, AGE INT, OCCUPATION TEXT );")

conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Bart Simpson', 'Male', 10, 'Student')");

conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Homer Simpson', 'Male', 40, 'Nuclear Plant')");

conn.execute("INSERT INTO SIMPSON_INFO (NAME, GENDER, AGE, OCCUPATION) VALUES ('Lisa Simpson', 'Female', 8, 'Student')");

conn.commit()

# print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes

------------------------------
#Retrieving certain data from tables
import sqlite3

# Connect to database 'simpsons.db'
conn = sqlite3.connect('simpsons.db')

# Searching by character name
# Get data from database
cursor = conn.execute("SELECT * from SIMPSON_INFO where NAME='Homer Simpson'")

# Extract data from cursor
rows = cursor.fetchall()
print 'Results for Homer Simpson:'
print rows

------------------------------------------
#Updating data inside tables and columns
import sqlite3

conn = sqlite3.connect('simpsons.db')
#updated Homer's age to 41
conn.execute("UPDATE SIMPSON_INFO set AGE=41 where NAME='Homer Simpson'")

conn.commit()

# print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes

cursor = conn.execute("SELECT * from SIMPSON_INFO")

rows = cursor.fetchall()
print rows

--------------------------------
#Deleting Tables 

import sqlite3

conn = sqlite3.connect('simpsons.db')

conn.execute("DROP TABLE SIMPSON_INFO")

conn.commit()

# print number of changes to database
changes = conn.total_changes
print "Number of changes:", changes

cursor = conn.execute("SELECT * from SIMPSON_INFO")

rows = cursor.fetchall()
print rows
