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

    @app.route("/recipe/add")
    def add_recipe():
        from document.meal import Meal
        name = request.args.get("name")
        serving = int(request.args.get("serving"))
        ingredient1 = Ingredient("apple","lb",1)
        ingredient2 = Ingredient("pear","lb",1)
        ingredients = [ingredient1,ingredient2]
        recipe = Meal(name,serving,1,1,ingredients,"non",1,"sweet",'None',2)
        recipe.save()
        return ('ok')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        return render_template("base.html")

    return app
