from django.contrib.auth.models import User


def get_user_by_username(username: str):
    user = User.objects.filter(username=username).first()
    return user


def is_admin_test(user: User):
    return user.is_staff


def is_owner_test(user: User):
    return not user.is_staff
