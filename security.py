"""
This module contains basic user authorization for the JWT token
You need to access http://127.0.0.1:5000/auth with POST request 
and send the below body as JSON.
{
	"username" : "admin",
	"password" : "admin"
}
and you will get jwt as access_token
	"access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTMzNDU5MzksImlhdCI6MTY1MzM0NTYzOSwibmJmIjoxNjUzMzQ1NjM5LCJpZGVudGl0eSI6MX0.pAq5R-mGII0oIAOSvkjDMyhPeiv7epgGBiU0f9Tsw7o"
TODO in a real world application user name and password should be kept encrypted
"""

from user import User

users = [
    User(1,'admin','admin')
]

user_name_mapping = {u.username: u for u in users}
user_id_mapping =  {u.id: u for u in users}

def authenticate(name,password):
    customer = user_name_mapping.get(name,None)
    if customer and customer.password == password:
        return customer

def identity(payload):
    customer_id = payload['identity'] 
    return user_id_mapping.get(customer_id, None)      