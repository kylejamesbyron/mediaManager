# mediaManaged
# a media database manager.

# Import sqlite and os calls

import sqlite3
connection = sqlite3.connect("girls.db")
cursor = connection.cursor()

#import linux os calls
import os


#Collecting the name.


selection = cursor.execute("SELECT name from girls")
for row in selection:
	userName = (row[0])
	fileName = ("pages/" + userName + ".html")
	print(row[0])
	print(fileName)
	f = open(fileName, 'a')