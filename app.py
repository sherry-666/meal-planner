from flask import jsonify, Flask, render_template, url_for, json
from core.mongo import initialize_mongo
from document.ingredient import Ingredient
import json


def create_app(test_config = None):
    #create and configure the app
    with open('config.json') as f:
        config = json.load(f)
    initialize_mongo(config["mongo_config"])
    app = Flask(__name__)

    # a simple page that says hello
    @app.route('/home')
    def hello():
        return 'Home Page'

    from api import generate_grocery_list
    app.register_blueprint(generate_grocery_list.bp)

    @app.route('/ingredient-library')
    def get_ingredient():
        from document.ingredient import Ingredient
        ingredients = Ingredient.get_ingredients()
        buffer = ""
        for ingredient in ingredients:
            buffer += ingredient.display()
        return buffer


    return app



#
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# @app.route('/get_meal')
# def get_meal():
#     return jsonify({"name":"Chicken with Broccoli","ingredient":["Chicken Breast","Broccoli"]}, {"name": "To