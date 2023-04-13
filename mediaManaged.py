# mediaManaged
# a media database manager.

# Import sqlite and os calls

import sqlite3
connection = sqlite3.connect("girls.db")
cursor = connection.cursor()

#import linux os calls
import os


#Collecting the name.


selection = cursor.execute("SELECT name, link from girls")
for row in selection:
	userName = (row[0])
	image = (row[1])
	fileName = ("pages/" + userName + ".html")
	print(row[0])
	print(fileName)
	f = open(fileName, 'w')
# Create pages:

#create header
	f.write('''
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
	<html>
	<head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
	<title>''')
#add title
	f.write("	" + userName)
#close title
	f.write('''</title></head> ''')

#Open body
	f.write('''
	<body>''')

	f.write("Name: "), f.write(userName)
	f.write("<br>")
	f.write("Age:  ")
	f.write("<br>")
	f.write("Location:  ")
	f.write('''
	<br>
	<br>
	<br>	
	<img style="width: 232px; height: 280px;" alt="Profile Picture"
	src="file://''')
	
	f.write(image)
	f.write('">')
#Close body
	f.write('''
	</body>

	</html> ''')

#Close file.
	f.close()