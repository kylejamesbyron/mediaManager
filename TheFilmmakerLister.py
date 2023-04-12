# The Filmmaker Lister

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("girls.db")
cursor = connection.cursor()

#import linux os calls
import os

#rows = cursor.execute("SELECT name, link FROM girls WHERE name = name")
#or row in rows:
#	print(row)
#print(rows)

searchName = "Amber"
selection = cursor.execute("SELECT name from girls")
for row in selection:
	inputer = (row[0])
	print(row[1])
	

	

connection.close()