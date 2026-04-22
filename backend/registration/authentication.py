from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # username = email in your login form
        print("EmailBackend called with:", username)
        if not username or not password:
            print("Missing username or password")
            return None

        try:
            user = User.objects.get(email=username)
            print("User found:", user)
        except User.DoesNotExist:
            print("User not found")
            return None

        if user.check_password(password):
            print("Password correct")
            return user
        else:
            print("Password incorrect")
            return None
        # if not username or not password:
        #     return None

        # try:
        #     user = User.objects.get(email=username)
        # except User.DoesNotExist:
        #     return None

        # if user.check_password(password) and user.is_active:
        #     return user

        # return None

