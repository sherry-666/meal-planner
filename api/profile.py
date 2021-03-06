from flask import Blueprint, jsonify, json, request
from lib.profile import get_or_create_profile, initiate_family_member
from document.profile import Profile
from mongoengine import *
from enum import IntEnum

profile_bp = Blueprint("profile", __name__, url_prefix="/api/profile")


@profile_bp.route("/add-member", methods=["POST"])
def add_family_member():
    member_info = json.loads(request.data)
    username = member_info.get("username")
    family_member = initiate_family_member(
        name=member_info.get("name"),
        year_of_birth=member_info.get("yearOfBirth"),
        weight=member_info.get("weight"),
        height=member_info.get("height"),
        activity_level=member_info.get("activityLevel"),
        gender=member_info.get("gender"),
    )
    profile = get_or_create_profile(username)
    profile.family_members.append(family_member)

    profile.save()
    return jsonify({
        "success": True
    })


@profile_bp.route("/get", methods=["GET"])
def get_profile():
    print(request.args.get('username', ''))
    username = request.args.get('username', '')
    profile = Profile.objects.get(username=username)
    print(profile)
    profile_json = profile.to_json()
    profile_data = json.loads(profile_json)
    return jsonify(profile_data)
