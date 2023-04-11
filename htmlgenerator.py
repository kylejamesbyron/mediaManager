
variable = "Testicles"
name = input("Name: ")
file = name + ".html"
print(file)

f = open(file, "a")
f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>''')
f.write(name)

f.write('''</title></head> ''')

f.write('''
	<body>''')

f.write("Name: "), f.write(name)

f.write('''

<pre>
	Does this compress whitespace.

''')

f.write("NAME:")
f.write(variable)

f.write('''
<img style="width: 232px; height: 280px;" alt="Christine Sitting"
src="file:///home/maisom/Documents/GitHub/mediaManager/users/Christine/67946633_001_86d3.jpg">

	</body>

</html>


''')

f.close()