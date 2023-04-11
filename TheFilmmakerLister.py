# The Filmmaker Lister

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("girls.db")
cursor = connection.cursor()

#import linux os calls
import os

rows = cursor.execute("SELECT name, link FROM girls WHERE name = name")
for row in rows:
	print(row)

connection.close()