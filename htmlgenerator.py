
variable = "Testicles"

f = open("7testhtml.html", "a")
f.write('''
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html><head><meta content="text/html; charset=ISO-8859-1" http-equiv="content-type">
<title>Test</title></head>

<body>

''')

f.write(variable)

f.write('''
</body>

</html>


''')

f.close()