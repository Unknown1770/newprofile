# importing Flask and other modules 
from flask import Flask, request, render_template 

# Flask constructor 
app = Flask(__name__) 

# A decorator used to tell the application 
<form action="{{ url_for("gfg")}}" method="post"> 
<label for="firstname">First Name:</label> 
<input type="text" id="firstname" name="fname" placeholder="firstname"> 
<label for="lastname">Last Name:</label> 
<input type="text" id="lastname" name="lname" placeholder="lastname"> 
<button type="submit">Login</button> 


# which URL is associated function 
@app.route('/', methods =["GET", "POST"]) 
def gfg(): 
	if request.method == "POST": 
	# getting input with name = fname in HTML form 
	first_name = request.form.get("fname") 
	# getting input with name = lname in HTML form 
	last_name = request.form.get("lname") 
	return "Your name is "+first_name + last_name 
	return render_template("form.html") 

if __name__=='__main__': 
app.run() 
