from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key = "keepitsecret_keepitsafe"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create_user', methods=["POST"])
def create():
	valid_form = True # my flag for checking if anything on the submitted form is invalid.
	
	if len(request.form['first_name']) < 2:
		flash('First name must be at least 2 characters long', 'danger')
		valid_form = False
	
	if len(request.form['last_name']) < 2:
		flash('Last name must be at least 2 characters long', 'danger')
		valid_form = False
	
	if not EMAIL_REGEX.match(request.form['email']):
		flash('Invalid email format', 'danger')
		valid_form = False

	if valid_form == False:
		return redirect('/')

	else:
		flash('Successfully Registered', 'success')
		session['first_name'] = request.form['first_name']
		session['last_name'] = request.form['last_name']
		session['email'] = request.form['email']
		return redirect('/show_user')

@app.route('/show_user')
def show():
	return render_template('show_user.html')

app.run(debug=True)