from api.ingredient import ingredient_bp
from api.recipe import recipe_bp
from api.auth import auth_bp

blueprints = [
    ingredient_bp,
    recipe_bp,
    auth_bp,
]