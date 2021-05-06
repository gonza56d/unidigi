# Django
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


UserModel = get_user_model()


class UserBackend(ModelBackend):
    """Authentication backend logic.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        """Implement authentication either by user or email, and password.
        """
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        username = username.lower()
        try:
            user = UserModel._default_manager.get(
                Q(username=username) | Q(email=username)
            )
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
