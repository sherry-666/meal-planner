from mongoengine import *
from enum import IntEnum


class FamilyMember(EmbeddedDocument):
    class Gender(IntEnum):
        Female = 1
        Male = 2

    # mapping from: reference: http://www.checkyourhealth.org/eat-healthy/cal_calculator.php
    class ActivityLevel(IntEnum):
        little = 1
        light = 2
        moderate = 3
        active = 4
        extra_active = 5

    ACTIVITY_LEVEL_FACTOR = {
        ActivityLevel.little: 1.2,
        ActivityLevel.light: 1.375,
        ActivityLevel.moderate: 1.55,
        ActivityLevel.active: 1.725,
        ActivityLevel.extra_active: 1.9,
    }
    name = StringField(required=True)
    year_of_birth = IntField(required=True)
    gender = IntField(required=True, choices=list(map(int, Gender)))
    weight = FloatField(required=True)
    height = FloatField(required=True)
    activity_level = IntField(required=True)
    cal = IntField(required=True)
    food_allergy = ListField(required=False)


class Profile(Document):
    username = StringField(required=True, primary_key=True)
    family_name = StringField(required=False)
    family_members = ListField(EmbeddedDocumentField(FamilyMember))
    total_cal = IntField(required=False)


