from document.profile import Profile
from mongoengine import DoesNotExist


def get_or_create_profile(username):
    try:
        profile = Profile.objects.get(username=username)
    except DoesNotExist:
        profile = Profile(username)
        profile.save()
    return profile
