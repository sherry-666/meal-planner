from flask import jsonify, Flask, render_template, url_for, json,request
from core.mongo import initialize_mongo
from document.ingredient import Ingredient
import json
from api import blueprints

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

    for bp in blueprints:
        app.register_blueprint(bp)

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
