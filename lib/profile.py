from document.profile import Profile, FamilyMember
from mongoengine import DoesNotExist
import datetime


def initiate_profile(username, family_name=None, family_members=[]):
    total_cal = 0
    for member in family_members:
        total_cal += member.cal

    total_cal = total_cal

    profile = Profile(
        username=username,
        family_name=family_name,
        family_members=family_members,
        total_cal=total_cal
    )
    return profile


def initiate_family_member(name, year_of_birth, weight, height, activity_level, gender, food_allergy=[]):
    # calculate cal: reference: http://www.checkyourhealth.org/eat-healthy/cal_calculator.php
    weight = int(weight)
    height = int(height)
    today = datetime.datetime.now()
    this_year = today.year
    age = this_year - int(year_of_birth)
    if gender == FamilyMember.Gender.Female:
        bmr = 655 + ((4.3 * weight) / 2.205) + ((4.7 * height) * 2.54) - (4.7 * age)
    else:
        bmr = 66 + ((6.3 * weight) / 2.205) + ((12.9 * height) * 2.54) - (6.8 * age)

    cal = bmr * FamilyMember.ACTIVITY_LEVEL_FACTOR.get(int(activity_level))
    cal = int(cal)
    food_allergy = food_allergy

    family_member = FamilyMember(
        name=name,
        year_of_birth=year_of_birth,
        weight=weight,
        height=height,
        activity_level=activity_level,
        gender=gender,
        cal=cal,
        food_allergy=food_allergy
    )
    return family_member


def get_or_create_profile(username):
    try:
        profile = Profile.objects.get(username=username)
    except DoesNotExist:
        profile = Profile(username)
        profile.save()
    return profile
