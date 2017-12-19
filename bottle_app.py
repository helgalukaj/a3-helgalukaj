
from bottle import route, run, default_app, debug, request

import csv

contents = []
with open("airline_safety.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

	

def htmlify(title,text):
    page = """
        <!doctype html>
        <html lang="en">
            <head>
                <meta charset="utf-8" />
                <title>%s</title>
                <style>
			body{
				background-color : #8FD3E7;
				text-align : center;
			}
			select{
				width:30%%;
				text-align:center;
			}
			table{
				margin-left:15%%;
				margin-right:15%%  ;
				border : 1,5 px solid black;
				width : 50%%;
				border-collapse:collapse;
			}
			th{
				height : 50px;
				background-color : #4CAF50;
				color : white;
			}
			td{
				border:1px solid black;
			}
			tr:hover{
				background-color : #C2C2C2;
			}
			.W{
				background-color : #26EF8A;
			}
			.L{
				background-color : #F74246;
			}
			a{
				font-size:25px;
				color:#878787;
			}
			a:hover{
				color:#961763;
			}
			.submit{
				width:10%%;
			}
		</style>
            </head>
            <body>
            %s
            </body>
        </html>

    """ % (title,text)
    return page

def index():
	text = """
	<form action="/airlinename" method="POST">
		<input type="textbox" name="airline" placeholder="Search By Airline Name"/>
		<input type="submit" value="Search">
	</form><br/>
	<form action="/year" method="POST">
		<select name="year">
			<option value="1">1985-1999</option>
			<option value="2">2000-2014</option>
		</select>
		<input type="submit" value="Search">
	</form><br/>
	<form action="/column" method="POST">
		<input type="checkbox" name="column" value="1">Incidents</input>
		<input type="checkbox" name="column" value="2">Accidents</input>
		<input type="checkbox" name="column" value="3">Fatalities</input><br/>
		<input type="submit" value="Search">
	</form><br/>
	<p>hffsgs8gs </p>
	
	"""
	return htmlify("My lovely website",text)

def airlinename():
	userinput = request.POST["airline"]
	text ="""<table>
			<tr>
				<th>Airline Name</th>
				<th>Kilometers Flown Every Week</th>
				<th>Incidents, 1985–1999</th>
				<th>Fatal Accidents, 1985–1999</th>
				<th>Fatalities, 1985–1999</th>
				<th>Incidents, 2000–2014</th>
				<th>Fatal Accidents, 2000–2014</th>
				<th>Fatalities, 2000–2014</th>
			</tr>\n	
				"""
	for x in contents :
		if userinput in x[0]:
			text += """<tr>
					<td>%(airlinename)s</td>
					<td>%(seat)s</td>
					<td>%(i8599)s</td>
					<td>%(a8599)s</td>
					<td>%(f8599)s</td>
					<td>%(i0015)s</td>
					<td>%(a0015)s</td>
					<td>%(f0015)s</td>
				</tr>
			""" % {"seat" : x[1], "airlinename":x[0], "i8599":x[2], "a8599":x[3], "f8599":x[4], "i0015":x[5], "a0015":x[6] ,"f0015":x[7]}
	text += "</table>"
	return htmlify("Title", text)

def year():
	userinput = request.POST["year"]
	text = ""
	if userinput == "1":
		text ="""<table>
			<tr>
				<th>Airline Name</th>
				<th>Incidents, 1985–1999</th>
				<th>Fatal Accidents, 1985–1999</th>
				<th>Fatalities, 1985–1999</th>
			</tr>\n	
				"""
		for x in contents :
			if x[0] == "AIRLINE":
				continue
			text += """<tr>
				<td>%(airlinename)s</td>
				<td>%(i8599)s</td>
				<td>%(a8599)s</td>
				<td>%(f8599)s</td>
							</tr>
			""" % {"airlinename":x[0], "i8599":x[2], "a8599":x[3], "f8599":x[4]}		
	else :
		text ="""<table>
			<tr>
				<th>Airline Name</th>
				<th>Incidents, 2000–2014</th>
				<th>Fatal Accidents, 2000–2014</th>
				<th>Fatalities, 2000–2014</th>
			</tr>\n	
				"""
		for x in contents :
			if x[0] == "AIRLINE":
				continue
			text += """<tr>
				<td>%(airlinename)s</td>
				<td>%(i0015)s</td>
				<td>%(a0015)s</td>
				<td>%(f0015)s</td>
							</tr>
			""" % {"airlinename":x[0],"i0015":x[5], "a0015":x[6] ,"f0015":x[7]}					
	text += "</table>"
	return htmlify("Title", text)

def column():
	userinput = request.POST.getall("column")
	print(userinput)	
	text = """<table>
				<tr>
					<th>Airline Name</th>"""
	for inpt in userinput:
		print(inpt)
		if inpt == "1":
			print("1st header added")
			text += """
					<th>Incidents, 1985–1999</th>
					<th>Incidents, 2000–2014</th>
					"""
		if inpt == "2":
			print("2nd header added")
			text += """
					<th>Fatal Accidents, 1985–1999</th>
					<th>Fatal Accidents, 2000–2014</th>
					"""
		if inpt == "3":
			print("Third header added")
			text += """
					<th>Fatalities, 1985–1999</th>
					<th>Fatalities, 2000–2014</th>
					"""
			print (text)		
	text += """		</tr>\n"""
	for x in contents:
		if x[0] == "AIRLINE":
				continue
		text += """<tr>
					<td>%s</td>"""	% x[0]
		for inpt in userinput :
			if inpt =="1":
				text += """
					<td>%(i8599)s</td>
					<td>%(i0015)s</td>
				""" % {"i8599":x[2], "i0015":x[5]}
			elif inpt =="2":
				text += """
					<td>%(a8599)s</td>
					<td>%(a0015)s</td>
				""" % {"a8599":x[3], "a0015":x[6]}
			elif inpt =="3":
				text += """
					<td>%(f8599)s</td>
					<td>%(f0015)s</td>
				""" % {"f8599":x[4], "f0015":x[7]}
		text += """		</tr>\n"""
	text += """	</table>\n"""						
	return htmlify("Title", text)

route('/', 'GET', index)
route('/airlinename', 'POST', airlinename)
route('/year', 'POST', year)
route('/column', 'POST', column)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

