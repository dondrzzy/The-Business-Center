[![Build Status](https://travis-ci.org/dondrzzy/The-Business-Center.svg?branch=master)](https://travis-ci.org/dondrzzy/The-Business-Center)
[![Coverage Status](https://coveralls.io/repos/github/dondrzzy/The-Business-Center/badge.svg)](https://coveralls.io/github/dondrzzy/The-Business-Center)
# The-Business-Center
The one stop center to boost your business


# THE API

These API application is live hosted with heroku [link](https://the-business-center.herokuapp.com)


The API enables you to create a user account, login with jwt authentication, create a business account after successfully logging in. 
Routes for getting all businesses arent protected, anyone can fetch all businesses but must login to post reviews about a business.
Only creator of businesses can update and delete them.
The jwt tokn is valid for exactly 60 seconds and you will be required to login again


The end points/Routes

`/api/auth/register` - to register 
```{
  "name":"xxx",
  "email":"x@gmail.com",
  "password":"1234"
  "password_c":"1234"
}
``` 


`/api/auth/login` - to login
```
{
  "email":"x@gmail.com",
  "password":"1234"
}
```

`/api/auth/reset-password` - to reset password

```
{
  "email":"x@gmail.com",
  "password":"1234"
  "password_c":"1234"
}
```


GET `/api/v1/businesses` - to get all businesses

POST `/api/businesses` - to create a business. APPI is interractive and will let you know of the missing fields

PUT `api/bussinesses/<businessId>` to update a business. Must be loggged in
  
DELETE `/api/businesses/<businessId>` to delete a business. Must be loggged in
  
GET  `/api/businesses/<businessId>` - to get a specific business
  
POST  `/api/businesses/<businessId>/reviews` - to post reviews to a business - Must be logged in to track user
  
GET  `/api/businesses/<businessId>/reviews` - to get all business reviews
  
  




