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
        return 'added'

    @app.route("/ingredient/add")
    def add_ingredient():
        from document.ingredientMacros import IngredientMacros
        name = request.args.get("name")
        measurement = request.args.get("measurement")
        carbs = float(request.args.get("carbs"))
        fat = float(request.args.get("fat"))
        protein = float(request.args.get("protein"))
        cal = float(request.args.get("cal"))
        ingredient_macros = IngredientMacros(
            name = name,
            measurement = measurement,
            carbs = carbs,
            fat = fat,
            protein = protein,
            cal = cal
        )
        ingredient_macros.save()
        return 'added'

    @app.route("/ingredient/get")
    def get_ingredient():
        from document.ingredientMacros import IngredientMacros
        ingredients = []
        for ingredient in IngredientMacros.objects:
            ingredient_json = ingredient.to_json()
            ingredient_data = json.loads(ingredient_json)
            ingredients.append(ingredient_data)
        return jsonify(ingredients)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        return render_template("base.html")

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    return app
