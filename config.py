import os
basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'canonical_test'
SQL_ALCHEMY_DATABASE_URI = 'sqlite:///customers.db'