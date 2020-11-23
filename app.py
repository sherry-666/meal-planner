from flask import jsonify, Flask, render_template, url_for, json,request
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

    @app.route("/api/ingredient/display")
    def get_ingredient():
        from document.ingredient import Ingredient
        ingredients = Ingredient.get_ingredients()
        buffer = ""
        for ingredient in ingredients:
            buffer += ingredient.display()
        return buffer

    @app.route("/api/ingredient/add")
    def add_ingredient():
        from document.ingredient import Ingredient
        name = request.args.get("name")
        measurement = request.args.get("measurement")
        quantity = int(request.args.get("quantity"))
        ingredient = Ingredient(name,measurement,quantity)
        ingredient.save()
        return ("ok")

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        return render_template("base.html")

    return app

