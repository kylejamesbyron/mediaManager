
variable = "Testicles"
name = input("Name: ")
file = name + ".html"
print(file)

f = open(file, "a")
f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Test</title></head>

<body>
<pre>
	Does this compress whitespace.

''')

f.write("NAME:")
f.write(variable)

f.write('''
</pre>	
</body>

</html>


''')

f.close()