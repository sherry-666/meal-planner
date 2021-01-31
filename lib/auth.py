from document.userAuth import UserAuth


def find_by_username(username):
    return UserAuth.objects.get(username=username)
