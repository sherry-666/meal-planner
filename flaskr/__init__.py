import os

from flask import Flask
from flask import jsonify, Flask, render_template, url_for, json



def create_app(test_config = None):
    #create and configure the app
    app = Flask(__name__)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

        # a simple page that says hello
    @app.route('/home')
    def hello():
        return 'Home Page'

        # register page
    from . import auth
    app.register_blueprint(auth.bp)

    from . import generate_grocery_list
    app.register_blueprint(generate_grocery_list.bp)

    from . import db
    db.init_app(app)

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