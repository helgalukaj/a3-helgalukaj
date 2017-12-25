
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
				background-color : #DCD5D5;
				text-align : center;
				background-image:url("https://travel.jumia.com/blog/ng/wp-content/uploads/2016/08/airplane-wallpaper-2.jpg");
				background-size: cover; 
				position: relative;
	
			}
			select{
				width:30%%;
				text-align:center;
			}
			table{
				margin-left:25%%;
				border : 1.5 px solid black;
				width : 50%%;
				border-collapse:collapse;
			}
			th{
				height : 30px;
				background-color : #000000;
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
				background-color : #F95D5D;
			}
			a{
				font-size:25px;
				color:#000000;
			}
			a:hover{
				color:#165070;
			}
			.submit{
				width:15%%;
			}
			p{
			text-align : center;
			margin-right: 80px;
			margin-left: 80px;
			font-family: 'BenchNine', sans-serif;
			
			text-shadow: white 90px 90px 90px;
			background-color:rgba(170,170,170,0.4);
			}
			h1  {
			text-align:center;
			font-weight: bold;
			color: #4D4D4D;
			font-size: 90px;
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
	<h1>Airline Safety</h1>
	<h2>"Aviation safety costs little,but saves much."</h2>
	<p>Safety of passengers in one of the most impotant thing we should consider when rating an airline.
	People should choose their flying companies carefully 
	by considering many factors,but the most important one should be being secure.This web app will 
	help everyone to check over some data and think over their choice
	</p>
	<form action="/airlinename" method="POST">
		<input type="text" name="airline" placeholder="Search By Airline Name"/>
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
		<input type="checkbox" name="column" value="1"/><label>Incidents</label>
		<input type="checkbox" name="column" value="2"/><label>Accidents</label>
		<input type="checkbox" name="column" value="3"/><label>Fatalities</label><br/>
		<input type="submit" value="Search">
	</form><br/>
	<p>The dataset was collected over 54 airline companies.It involves number of km they fly in a week and 
	number of incidents, fatalities and fatal accidents.This web app will help you compare the progress airlines
	made from their beginnings 1985-1999 to these days 2000-2014.Check our web app to be sure if the company you are choosing is the
	right one and if this company gives priority to its clients by  making their crafts more secure.If the number of incidents
	is lower year by year this means that the airline invested to improve the quality.
	</p>
	<a href="https://github.com/ituis17/a3-helgalukaj">Assignment page</a>
	"""
	return htmlify("Airline safety",text)

def addrow(x):
	text = """<tr>
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
	return text
def create_header(text):
	text1 = """<table>
			<tr>
				%s
			</tr>\n	
				""" %text
	return text1		

def airlinename():
	userinput = request.POST["airline"]
	header = """<th>Airline Name</th>
				<th>Kilometers Flown Every Week</th>
				<th>Incidents, 1985–1999</th>
				<th>Fatal Accidents, 1985–1999</th>
				<th>Fatalities, 1985–1999</th>
				<th>Incidents, 2000–2014</th>
				<th>Fatal Accidents, 2000–2014</th>
				<th>Fatalities, 2000–2014</th>"""
	text = create_header(header)
	for x in contents :
		if x[0] == "AIRLINE":
			continue
		if userinput in x[0]:
			text += addrow(x) 
	text += "</table>"
	return htmlify("Title", text)

		

def year():
	userinput = request.POST["year"]
	text = ""
	if userinput == "1":
		header = """<th>Airline Name</th>
				<th>Incidents, 1985–1999</th>
				<th>Fatal Accidents, 1985–1999</th>
				<th>Fatalities, 1985–1999</th>"""
		text =create_header(header)
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
		header = """<th>Airline Name</th>
				<th>Incidents, 2000–2014</th>
				<th>Fatal Accidents, 2000–2014</th>
				<th>Fatalities, 2000–2014</th>"""
		text =create_header(header)
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

