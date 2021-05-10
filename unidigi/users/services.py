"""Users business logic."""

# Django
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

# Unidigi
from .models import User


def log_in(username: str, password: str) -> None:
    """Handle user log in business logic.
    """
    user = authenticate(username=username, password=password)
    if not user:
        raise ValidationError('Invalid credentials.')
    return user


def sign_up(username: str, email: str, password: str, first_name: str,
            last_name: str, role: str) -> User:
    """Handle user sign up business logic.
    """
    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        role=role
    )
    return user
