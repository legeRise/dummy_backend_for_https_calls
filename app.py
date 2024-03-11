'''
dummy backend( on PythonAnywhere ):

Function:  make api calls to Original backend and return the response back to the original frontend which made
call on this(dummy backend)

Purpose: The frontend(React native app) does not support http calls hence and actual backend is too much for 
pythonAnywhere free tier --- hence a dummy backend to provide 'https' apis to frontend and actually making calls
back to original one

'''

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Define the base URL of your Django backend hosted on AWS EC2
BASE_URL = "http://54.151.177.70:8000/"

# Define routes to proxy requests to your Django backend
@app.route('/list_models/', methods=['GET'])
def list_models():
    response = requests.get(BASE_URL + '/list_models/')
    return jsonify(response.json())

@app.route('/model/<model_name>_predict/', methods=['POST'])
def predict(model_name):
    response = requests.post(BASE_URL + f'/model/{model_name.lower()}_predict/', json=request.json)
    return jsonify(response.json())

@app.route('/add_product/', methods=['POST'])
def add_product():
    response = requests.post(BASE_URL + '/add_product/', json=request.json)
    return jsonify(response.json())

@app.route('/list_products/', methods=['GET'])
def list_products():
    response = requests.get(BASE_URL + '/list_products/')
    return jsonify(response.json())

