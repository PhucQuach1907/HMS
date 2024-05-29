from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password

from user_info.models import User


class CustomBackend(BaseBackend):
    def authenticate(self, request, login_id=None, password=None, **kwargs):
        try:
            user = User.objects.get(login_id=login_id)
            print(password, user.password)
            if check_password(password, user.password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
