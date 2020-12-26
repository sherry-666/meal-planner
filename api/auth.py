#authentication validation
from flask import Blueprint, request, jsonify
from document.userAuth import UserAuth
import json
from flask_login import login_user, current_user

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    user_info = json.loads(request.data)
    username = user_info.get("username")
    password = user_info.get("password")
    user = UserAuth.objects.get(username=username)
    # TODO: encrypt password
    if password != user.password:
        return jsonify({
            "success": False
        })
    print(current_user)
    login_user(user, remember=True)
    print(current_user)
    print("user log in !!!")
    return jsonify({
        "success": True
    })

@auth_bp.route("/register", methods=["POST"])
def register():
    user_info = json.loads(request.data)
    username = user_info.get("username")
    password = user_info.get("password")
    user_auth = UserAuth(
        username=username,
        password=password
    )
    # TODO: Add password encryption in database, cookie, and existing username check
    user_auth.save()
    return jsonify({
        "success": True
    })
