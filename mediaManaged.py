# mediaManaged
# a media database manager.

# Begin Open

# Import sqlite
import sqlite3
connection = sqlite3.connect("girls.db")
cursor = connection.cursor()

#import linux os calls
import os

#import flask

from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
from flask import session
from flask import redirect

#import from datetime
import datetime
from datetime import datetime
from datetime import date
from datetime import time 


#flask business
app = Flask(__name__)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# End of opening


#Collecting the name.

selection = cursor.execute("SELECT name, link, age, location from girls")
for row in selection:
	userName = (row[0])
	image = (row[1])
	age = (row[2])
	location = (row[3])
	fileName = ("pages/" + userName + ".html")
	print(row[0])
	print(fileName)
	f = open(fileName, 'w')


# Create pages:

#create header
	f.write('''
	<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" \
	"http://www.w3.org/TR/html4/strict.dtd">
	<html>
	<head><meta content="text/html; charset=ISO-8859-1" \
	http-equiv="content-type">
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
	f.write("Age:  "), f.write(str(age))
	f.write("<br>")
	f.write("Location:  "), f.write(location)
	f.write('''
	<br>
	<br>
	<br>	
	<img style="width: 516px; height: 368px;" alt="profile"
	src="file://''')
	
	f.write(image)
	f.write('">')
#Close body
	f.write('''
	</body>

	</html> ''')

#Close file.
	f.close()


# Listing photo files
userdir = "users/"
for dirname in os.listdir(userdir):
	cursor.execute("INSERT OR IGNORE INTO girls (name) values (?)", [dirname])
	print("------------")
	print(dirname)
	print("------------")
	photodir = ("users/" + dirname)
	for photo in os.listdir(photodir):
		record = ("home/maisom/Documents/GitHub/mediaManager/users/" \
			+ dirname + "/" + photo)
#		print(record)
		cursor.execute("INSERT OR IGNORE INTO photos (name, link) values \
			(?, ?)", [dirname, record])
	#	print(photo)


#####<<<< automatically look for picture names profile.	

connection.commit() 


# HOME

# Create Home page:

filenamed = ('templates/home.html')
f = open(filenamed, 'w')

#create header
f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" \
"http://www.w3.org/TR/html4/strict.dtd">
<html>
<head><meta content="text/html; charset=ISO-8859-1" \
http-equiv="content-type">
<title>''')
#add title
f.write("	" + 'home')
#close title
f.write('''</title></head> ''')

#Open body
f.write('''
<body>''')
f.write("Name: "), f.write(userName)
f.write("<br>")
f.write("Age:  "), f.write(str(age))
f.write("<br>")
f.write("Location:  "), f.write(location)
f.write('''
<br>
<br>
<br>	
<img style="width: 516px; height: 368px;" alt="profile"
src="file://''')
	
f.write(image)
f.write('">')
#Close body
f.write('''
</body>

</html> ''')

#Close file.
f.close()

@app.route('/')
def home():
	return render_template('home.html')





# Close Flask
if __name__ == '__main__':
   app.run(debug = True)

