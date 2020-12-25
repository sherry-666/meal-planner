from flask import Blueprint, request
from document.meal import Meal
from document.ingredient import Ingredient
recipe_bp = Blueprint("recipe", __name__, url_prefix="/api/recipe")

@recipe_bp.route("/add")
def add_recipe():
    name = request.args.get("name")
    serving = int(request.args.get("serving"))
    ingredient1 = Ingredient("apple", "lb", 1)
    ingredient2 = Ingredient("pear", "lb", 1)
    ingredients = [ingredient1, ingredient2]
    recipe = Meal(name, serving, 1, 1, ingredients, "non", 1, "sweet", "None", 2)
    recipe.save()
    return "added"