#!/usr/bin/python
import MySQLdb

# Setup MySQL Connection
db = MySQLdb.connect(host="localhost", user="root", passwd="python", db="cards")
cursor = db.cursor()

# Insert a row into our table
cursor.execute("INSERT INTO users (firstname) VALUES ('Keenan')")

# Save changes to database
db.commit()