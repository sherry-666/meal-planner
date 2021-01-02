from mongoengine import *
import datetime
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

    activity_level_factor = {
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
    food_allergy = LineStringField(required=False)

    # constructor
    def __int__(self, name, year_of_birth, weight, height, activity_level, gender, food_allergy):
        super().__int__()
        self.name = name
        self.year_of_birth = year_of_birth
        self.weight = weight
        self.height = height
        self.activity_level = activity_level
        self.gender = gender

        # calculate cal: reference: http://www.checkyourhealth.org/eat-healthy/cal_calculator.php
        today = datetime.datetime.now()
        this_year = today.year
        age = this_year - self.year_of_birth
        if self.gender == "female":
            bmr = 655 + ((4.3 * self.weight) / 2.205) + ((4.7 * self.height) * 2.54) - (4.7 * age)
        else:
            bmr = 66 + ((6.3 * self.weight) / 2.205) + ((12.9 * self.height) * 2.54) - (6.8 * age)

        cal = bmr * self.activity_level_factor.get(activity_level)
        self.cal = int(cal)
        self.food_allergy = food_allergy


class Profile(Document):
    family_name = StringField(required=True)
    family_members = ListField(EmbeddedDocumentField(FamilyMember))
    total_cal = IntField(required=True)

    # constructor
    def __init__(self, family_name, family_members):
        super().__init__()
        self.family_name = family_name
        self.family_members = family_members

        total_cal = 0
        for member in family_members:
            total_cal += member.cal

        self.total_cal = total_cal
