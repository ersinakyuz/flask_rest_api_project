import config 
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
app.secret_key = 'canonical_test'

app.config.from_object("config")
#config.init_app(app)


API_URL= app.config['GIT_API_URL']

print(API_URL)