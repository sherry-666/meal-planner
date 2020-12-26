#authentication validation
from flask import Blueprint, request, jsonify
from document.userAuth import UserAuth
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

@auth_bp.route("/register", methods=["POST"])
def register():
    user_info = json.loads(request.data)
    username = user_info.get("username")
    password = user_info.get("password")
    print(username, password)
    user_auth = UserAuth(
        username=username,
        password=password
    )
    # TODO: Add password encryption in database, cookie, and existing username check
    user_auth.save()
    return jsonify({
        "success": True
    })



