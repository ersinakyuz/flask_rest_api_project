from queue import Empty
import sqlite3
from flask import jsonify
from flask_jwt import JWT, jwt_required, current_identity
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models.customer import CustomerModel
from db import db

customer_put_args = reqparse.RequestParser()
customer_put_args.add_argument("name", type=str, help="Name of the Customer is required", required = True)
customer_put_args.add_argument("is_active", type=str, help="Is the Customer active", default = True)
customer_put_args.add_argument("bills", type=str, help="Bills of the Customer", default = 0)

resource_fields = {
    'id'        : fields.Integer,
    'name'      : fields.String,
    'is_active' : fields.Integer,
    'bills'     : fields.Integer
}



class Customer(Resource):
    #@jwt_required()
    @marshal_with(resource_fields)
    def get(self, customer_id):
        result = CustomerModel.query.filter_by(id = customer_id).first()
        if not result:
            abort(404, message = "ID does not exists")
        return result
        
    """
    Add a customer 
    """
    @jwt_required()
    def put(self, customer_id):
        args = customer_put_args.parse_args()
        result = CustomerModel.query.filter_by(id = customer_id).first()
        if args['name'] is "":
            abort(400, message = "Name is missing")
        if result:
            abort(409, message = "ID is exists")
        customer = CustomerModel (id = customer_id, name = args['name'], is_active = args['is_active'], bills = args['bills'], )
        db.session.add(customer)
        db.session.commit()
        return customer.json(), 201

    """
    Modify the customer data with PATCH
    """
    #@jwt_required()
    @marshal_with(resource_fields)
    def patch(self, customer_id):
        args = customer_put_args.parse_args()
        result = CustomerModel.query.filter_by(id = customer_id).first()
        if args['name'] is "":
            abort(400, message = "Name is missing")
        if not result:
            abort(404, message = "ID does not exists")
        customer = CustomerModel (id = customer_id, name = args['name'], is_active = args['is_active'], bills = args['bills'], )
        db.session.merge(customer)
        db.session.commit()
        return result, 200      


    """
    Delete the customer 
    """
    #@jwt_required()
    def delete(self, customer_id):
        del customers[customer_id]
        return '', 204


class CustomerList(Resource):
    #@jwt_required()
    def get(self):
        result = CustomerModel.query.all()
        if not result:
            abort(404, message = "Record does not exists")
        else:
            output = []
            for customer in result:
                customer_data = {}
                customer_data['id'] = customer.id
                customer_data['name'] = customer.name
                customer_data['is_active'] = customer.is_active
                customer_data['bills'] = customer.bills

                output.append(customer_data)
            return jsonify({'users' : output})