# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/temperature', methods=['POST'])
def temperature():
    data = request.get_json()
    # Process the data
    return jsonify(data), 200