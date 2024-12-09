#!/usr/bin/python3
import cgi, cgitb
cgitb.enable()
print('Content-type:text/html \n')
x = 10/0
print('''
	<html>
		<head>
			<title>My First CGI Script</title>
		</head>
		<body>
			<h1>Hello World</h1>
		</body>
	</html>
''')