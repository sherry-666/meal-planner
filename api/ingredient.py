from flask import Blueprint, jsonify, json, request
from document.ingredientMacros import IngredientMacros

ingredient_bp = Blueprint("ingredient", __name__, url_prefix="/api/ingredient")

@ingredient_bp.route("/add")
def add_ingredient():
    name = request.args.get("name")
    measurement = request.args.get("measurement")
    carbs = float(request.args.get("carbs"))
    fat = float(request.args.get("fat"))
    protein = float(request.args.get("protein"))
    cal = float(request.args.get("cal"))
    ingredient_macros = IngredientMacros(
        name=name,
        measurement=measurement,
        carbs=carbs,
        fat=fat,
        protein=protein,
        cal=cal
    )
    ingredient_macros.save()
    return 'added'


@ingredient_bp.route("/get")
def get_ingredient():
    ingredients = []
    for ingredient in IngredientMacros.objects:
        ingredient_json = ingredient.to_json()
        ingredient_data = json.loads(ingredient_json)
        ingredients.append(ingredient_data)
    return jsonify(ingredients)