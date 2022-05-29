#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "1.0.0"
__author__ = "Ersin Akyuz"
__email__ = "ersinakyuz.de@gmail.com"
__description__ = "Python Rest API with Flask Sample"

from flask import Flask, render_template, request
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Api, Resource, reqparse, abort, marshal_with
from flask_sqlalchemy import SQLAlchemy

from security import authenticate, identity
from resources.customer import Customer, CustomerList
import config

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['SECRET_KEY']
api = Api(app)
jwt = JWT(app, authenticate, identity)


@app.before_first_request
def create_tables():
    app.logger.info("DB created before_first_request")
    db.create_all()

api.add_resource(Customer,"/customer/<int:customer_id>")
api.add_resource(CustomerList, '/customers')

#api.add_resource(Item,"/item/<int:item_id>")



if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port="5000", debug = True)