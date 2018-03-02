[![Build Status](https://travis-ci.org/dondrzzy/The-Business-Center.svg?branch=ft-api-postgres)](https://travis-ci.org/dondrzzy/The-Business-Center)
[![Coverage Status](https://coveralls.io/repos/github/dondrzzy/The-Business-Center/badge.svg?branch=ft-api-postgres)](https://coveralls.io/github/dondrzzy/The-Business-Center?branch=ft-api-postgres)
[![Code Climate](https://api.codeclimate.com/v1/badges/a1068bc6a624a1e673d6/maintainability.png)](https://github.com/dondrzzy/The-Business-Center)
# The-Business-Center API
The one stop center to boost your business

These API is currently live hosted with heroku [link](https://the-business-center-api.herokuapp.com)


The API enables you to create a user account, login with jwt authentication, create a business account after successfully logging in. 
Routes for getting all businesses arent protected, anyone can fetch all businesses but must login to post reviews about a business.
Only creator/owner of the businesses can update and delete them.
The jwt token is valid for exactly 30 minutes after which it expires and you will be required to login again.


## Getting Started

The following instructions will get you up and running with a copy of this API on your local machine for development, testing  and deployment purposes.

### How to run the API application

## Prerequisites
* [Python 3.6.4](https://www.python.org/downloads/)
* [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [Flask](http://flask.pocoo.org/)
* [Postgres](https://wiki.postgresql.org/wiki/Detailed_installation_guides)

###### Navigate to a directory where you would like to create your application

##### Clone the API repository using the link below

> https://github.com/dondrzzy/The-Business-Center.git


##### Create a virtual environment on your local machine

```
######   1.  Install virtualenv and create a virtual environment using this guide
   
   http://docs.python-guide.org/en/latest/dev/virtualenvs/

###### 2.  Install the application dependencies in the requirements.txt file

    open your terminal and run "pip3 -r install requirements.txt" 
```

#### Set up your database and Environment variables
    Make sure your postgres service is running. Check task manager processes for confirmation.
    
    Set up your postgres datase with a your "username" and "password"
    
    In the root directory of your application, create a .env file and set the following

    set DATABASE_URL="postgresql://{username}:{password}@localhost/{database_name}"
    set ENVIRON="development"


#### Run the migrations to create your database
  
    creae the migrations
    (venv)$ python manage.py db init
   
    create the Migrations script
    (venv)$ python manage.py db migrate
    
    Populate your databse with the tables
    (venv)$ python manage.py db upgrade


##### Start the application

> python run.py

Open your favorite browser, preferrably google chrome and route to  **[this location](http://127.0.0.1:5000/apidocs)** for instructions

You can also use postman to test the endpoints

### Usage

| Route End-Points                         | Functionality                            |
| ---------------------------------------- | ---------------------------------------- |
| POST /api/v1/auth/register                      | Register user for an account |
| POST /api/v1/auth/login                         | Login to your account                          |
| POST /api/v1/auth/reset-password                 | Reset your password accounnt                  |
| GET /api/v1/auth/logout                         | Logout of your account                          |
| POST /api/v1/businesses                      | Create a new Business              |
| GET /api/v1/businesses                      | Get all businesses             |
| GET /api/v1/businesses/{businessId}          | Get a single businesses             |
| PUT /api/v1/businesses/{businessId}          | Update a businesses             |
| DELETE /api/v1/businesses/{businessId}          | Delete a businesses             |
| POST /api/v1/businesses/{businessId}/reviews          | Ppost reviews to a business             |
| GET /api/v1/businesses/{businessId}/reviews          | Get a business' reviews             |


## Testing the Api

The application is tested using pytest with coverage. Install pytest to run your tests and in your terminal, run...

```
> pytest app
```

## Deployment

Follow this guide on how to deploy to the live environment.
```
[link](https://medium.com/@johnkagga/deploying-a-python-flask-app-to-heroku-41250bda27d0)
```
