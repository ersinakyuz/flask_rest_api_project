from db import db
"""
This module contains sample basic user model

TODO in a real-world application below fields can be added for user uniquity
Firstname,
Lastname,
Address,
Phone,
E-Mail,
etc.

"""

class CustomerModel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    is_active = db.Column(db.Integer, nullable = False)
    bills = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Customer(id = {id}, name = {name}, is_active = {is_active}, bills = {bills})"

    def __init__(self, id, name, is_active, bills):
        self.id = id
        self.name = name
        self.is_active = is_active
        self.bills = bills

    def json(self):
        return {'id':self.id, 'name': self.name, 'is_active': self.is_active, 'bills': self.bills}
