# importing Flask and other modules 
from flask import Flask, request, render_template 

# Flask constructor 
app = Flask(__name__) 

# A decorator used to tell the application 
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

@app.route('/karthik', methods =["GET", "POST"]) 
def gfgf(): 
	if request.method == "POST": 
	# getting input with name = fname in HTML form 
	first_name = request.form.get("fname") 
	return "Your name is "+first_name 
	return render_template("form.html") 

if __name__=='__main__': 
   #app.run()
   app.run(host='127.0.0.1', port=8080, debug=True)
