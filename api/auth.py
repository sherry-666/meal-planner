#authentication validation
from flask import Blueprint, request, jsonify
import json

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    user_info = json.loads(request.data)
    username = user_info.get("username")
    password = user_info.get("password")
    print(username, password)
    # TODO: Add username password verification
    return jsonify({
        "success": True
    })

@auth_bp.route("/register")
def register():

    return "Registration Successful"



