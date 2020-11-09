from flask import Flask
app = Flask(__name__)
from flask import jsonify

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/get_meal')
def get_meal():
    return jsonify([{"name": "Fried Fish"}, {"name": "Tomato Egg"}])