from flask import jsonify, Flask, render_template, url_for, json
from core.mongo import initialize_mongo
from document.ingredient import Ingredient
import json


def create_app(test_config = None):
    #create and configure the app
    with open("config.json") as f:
        config = json.load(f)
    initialize_mongo(config["mongo_config"])
    app = Flask(
        __name__,
        template_folder="frontend/templates",
        static_folder="frontend/dist",
    )

    @app.route("/")
    def react():
        return render_template("base.html")

    @app.route("/bundle.js")
    def dist_file():
        return app.send_static_file("bundle.js")

    # a simple page that says hello
    @app.route("/home")
    def hello():
        return "Home Page"

    from api import generate_grocery_list
    app.register_blueprint(generate_grocery_list.bp)

    @app.route("/ingredient-library")
    def get_ingredient():
        from document.ingredient import Ingredient
        ingredients = Ingredient.get_ingredients()
        buffer = ""
        for ingredient in ingredients:
            buffer += ingredient.display()
        return buffer
    return app
