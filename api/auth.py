# authentication validation
from flask import Blueprint, request, jsonify
from document.userAuth import UserAuth
import json
from flask_login import login_user, current_user, logout_user, login_required
from mongoengine import DoesNotExist

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_bp.route("/login", methods=["POST"])
def login():
    user_info = json.loads(request.data)
    username = user_info.get("username")
    password = user_info.get("password")
    # user = UserAuth.objects.get(username=username)

    try:
        user = UserAuth.objects.get(username=username)
        if password != user.password:
            return jsonify({
                "success": False
            })
        login_user(user, remember=True)
        return jsonify({
            "success": True
        })
    except DoesNotExist:
        return jsonify({
            "success": False
        })


@auth_bp.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({
        "logout": True
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
