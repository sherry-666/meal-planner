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
        static_folder="frontend/static",
    )

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

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        return render_template("base.html")

    return app

