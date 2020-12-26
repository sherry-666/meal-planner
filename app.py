from flask import Flask, render_template
from core.mongo import initialize_mongo
from core.auth import initialize_auth
from api import blueprints
from flask_login import current_user
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
    app.secret_key = config["flask"]["secret_key"]

    initialize_auth(app)

    # Register all blueprints.
    for bp in blueprints:
        app.register_blueprint(bp)

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def react(path):
        logged_in_user = None
        if current_user.is_authenticated:
            logged_in_user = current_user.to_dict()
        return render_template(
            "base.html",
            logged_in_user=json.dumps(logged_in_user)
        )

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    return app
