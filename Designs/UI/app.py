from flask import Flask, render_template, flash, redirect, url_for, logging, request


app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def user_login():
	if request.method == 'POST':
		email = request.form['email']
		password_candidate  = request.form['password']		

		flash('Successfully logged in', 'success')

		return redirect(url_for('dashboard'))
			
	return render_template('user_login.html')

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method == 'POST':		
		name = request.form['name']
		email = request.form['email']
		password = request.form['password']

		flash('You are now registered and can login', 'success')

		return  redirect(url_for('user_login'))
	
	return render_template('user_signup.html')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html')

@app.route('/business_register', methods=['GET', 'POST'])
def b_register():
	if request.method == 'POST':
		return redirect(url_for('businesses'))
	return render_template('business_register.html')

@app.route('/businesses')
def businesses():
	return render_template('businesses.html')

@app.route('/business/<string:id>', methods=['GET', 'POST'])
def read_business(id):
	return render_template('business.html', id=id)

@app.route('/edit/business/<string:id>', methods=['GET','POST'])
def edit_business(id):
	return render_template('update_business.html')

@app.route('/delete/business/<string:id>', methods=['DELETE'])
def delete_business(id):
	return ''

@app.route('/review/business/<string:id>', methods=['GET', 'POST'])
def review_business(id):
	return render_template('review_business.html', id=id)

if(__name__) == '__main__':
	app.run(debug=True, port=5000)