from flask import Blueprint, jsonify, json, request
from document.profile import FamilyMember, Profile
from mongoengine import *

profile_bp = Blueprint("profile", __name__, url_prefix="/api/profile")


@profile_bp.route("/add-member", methods=["POST"])
def add_family_member():
    member_info = json.loads(request.data)
    username = member_info.get("username")
    family_member = FamilyMember(
        name=member_info.get("name"),
        year_of_birth=member_info.get("year_of_birth"),
        weight=member_info.get("name"),
        height=member_info.get("weight"),
        activity_level=1,
        gender=1,
        # activity_level=member_info.get("activity_level"),
        # gender=member_info.get("gender")
    )
    total_cal = IntField(required=True)
    profile.family_members.append(family_member)
    profile.save()
    return jsonify({
        "success": True
    })
