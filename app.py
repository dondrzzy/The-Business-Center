from flask import Flask, request, jsonify, render_template, url_for, session
from models.user import User
from models.business import Business
from models.review import Review

User = User()
Business = Business()
Review = Review()

app = Flask(__name__)


app.config['SECRET_KEY'] = 'secret'

@app.route('/', methods=["GET"])
def index():
	return jsonify({"try":"/api/v1/auth/register"})

@app.route('/api/auth/register', methods=['POST'])
def register():
	data = request.get_json()
	if "name" not in data:
		return jsonify({"success":False, "msg":"name is required"})
	elif "email" not in data:
		return jsonify({"success":False, "msg":"email is required"})
	elif "password" not in data:
		return jsonify({"success":False, "msg":"password is required"})
	elif "password_c" not in data:
		return jsonify({"success":False, "msg":"password_c is required"})
	elif data["password"] != data["password_c"]:
		return jsonify({"success":False, "msg":"passwords do not match"})

	user_obj = {
		"name" : data["name"],
		"email" : data["email"],
		"password" : data["password"]
	}

	if User.register(user_obj):
		return jsonify({"success":True, "msg":"User Registered Successfully", "users":User.getUsers()})

	return jsonify({"success":False, "msg":"email is taken"})

@app.route('/api/auth/login', methods=['POST'])
def login():

	data = request.get_json()

	if "email" not in data:
		return jsonify({"success":False, "msg":"email is required"})
	if "password" not in data:
		return jsonify({"success":False, "msg":"password is required"})

	user_obj = {
		"email" : data["email"],
		"password" : data["password"]
	}

	if "email" in session and session["email"] == data["email"]:
		return jsonify({"success":False, "msg":"Already logged in. Redirecting..."})

	res = User.login(user_obj)
	pprint(res)
	if res["success"] and res["pwd"]:
		session['logged_in'] = True
		session['email'] = data['email']
		return jsonify({"success":True, "msg":"Successfully logged in. Redirecting to dashboard..."})
	elif res["success"] and not res["pwd"]:
		return jsonify({"success":False, "msg":"email and password mismatch"})
	return jsonify({"success":False, "msg":"User Not Found"})

@app.route('/api/auth/logout', methods=['POST'])
def logout():
	session.clear()
	return jsonify({"success":True, "msg":"You are logged out"})

@app.route('/api/auth/reset-password', methods=['POST'])
def reset_password():
	data = request.get_json()
	if "email" not in data:
		return jsonify({"success":False, "msg":"email is required"})
	elif "password" not in data:
		return jsonify({"success":False, "msg":"password is required"})
	elif "password_c" not in data:
		return jsonify({"success":False, "msg":"password_c is required"})
	elif data["password"] != data["password_c"]:
		return jsonify({"success":False, "msg":"passwords do not match"})
	user_obj = {
		"email" : data["email"],
		"password" : data["password"]
	}

	if User.resetPassword(user_obj):
		return jsonify({"success":True, "msg":"Password reset successfully"})
	return jsonify({"success":False, "msg":"User not found"})

@app.route('/api/businesses', methods=['POST'])
def register_business():
	if "id" not in session:
		return jsonify({"success":False, "msg":"Access denied! Login"})
	data = request.get_json()
	if "name" not in data:
		return jsonify({"success":False, "msg":"business name ('name') is required"})
	elif "category" not in data:
		return jsonify({"success":False, "msg":"category is required"})
	elif "location" not in data:
		return jsonify({"success":False, "msg":"location is required"})

	
	
	b_obj = {
		"name" : data["name"],
		"category" : data["category"],
		"location" : data["location"],
		"user_id" : session["id"]
	}

	Business.registerBusiness(b_obj)
	return jsonify({"success":True, "msg":"Business Created", "businesses":Business.getAllBusinesses()})


@app.route('/api/businesses')
def get_all_businesses():
	return jsonify({"success":True, "businesses":Business.getAllBusinesses()})

@app.route('/api/businesses/<businessId>')
def get_business(businessId):
	res = Business.getBusiness(int(businessId))
	if res["found"]:
		return jsonify({"success":True, "businesses":res["business"]})
	return jsonify({"success":False, "msg":"Business with id "+businessId+" not found!"})
# incomplete
@app.route('/api/businesses/<businessId>', methods=['PUT'])
def update_business(businessId):
	data = request.get_json()
	b_obj = {}
	if "name" not in data and "category" not in data and "location" not in data:
		return jsonify({"success":False, "msg":"Nothing to update"})

	if "name" in data:
		b_obj["name"] = data["name"]
	if "category" in data:
		b_obj["category"] = data["category"]
	if "location" in data:
		b_obj["location"] = data["location"]


	if Business.updateBusiness(b_obj, int(businessId)):
		return jsonify({"success":True, "msg":"Business updated successfully", "businesses":Business.getAllBusinesses()})
	return jsonify({"succes":False, "businesses":Business.getAllBusinesses(), "msg":"Business with id "+ businessId+" not found"})


@app.route('/api/businesses/<businessId>', methods=['DELETE'])
def delete_business(businessId):
	if Business.deleteBusiness(int(businessId)):
		return jsonify({"success":True, "message":"Business deleted successfully", "businesses":Business.getAllBusinesses()})
	return jsonify({"success":False, "message":"Business with id "+businessId+ " not found"})


# Reviews
@app.route('/api/businesses/<businessId>/reviews', methods=['POST'])
def add_review(businessId):
	if "id" not in session:
		return jsonify({"success":False, "msg":"Access denied! Login"})
	
	data = request.get_json()
	print(data)
	if "text" not in data:
		return jsonify({"success":False, "msg":"Provide a review ('text')"})
	rev = {
		"text" : data["text"]
	}

	if Review.addReview(rev, int(businessId)):
		return jsonify({"success":True, "msg":"Review successfully added", "reviews":Review.getAllReviews()})
	return jsonify({"success":False, "msg":"Business with id "+businessId+" not found"})

@app.route('/api/businesses/<businessId>/review')
def get_business_eviews(businessId):
	return jsonify({"success":True, "reviews":Review.getBusinessReviews(int(businessId))})

if(__name__) == '__main__':
	app.run(debug=True)