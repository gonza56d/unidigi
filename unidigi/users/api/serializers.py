"""Users serializers."""

# Django
from django.core.exceptions import ValidationError

# DRF
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as DRFValidationError
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

# Unidigi
from ..models import User, Profile
from .. import services as user_services


class UserSerializer(serializers.ModelSerializer):
    """Serializer to represent User model.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'created', 'profile']


class UserSignUpSerializer(serializers.Serializer):
    """Serializer to define users' sign up.
    """

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, max_length=64)

    first_name = serializers.CharField(max_length=100)

    last_name = serializers.CharField(max_length=100)

    role = serializers.ChoiceField(choices=Profile.Roles.choices)

    def create(self, data):
        """Define user creation (signup).
        """
        user = user_services.sign_up(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role']
        )
        return user


class UserLogInSerializer(serializers.Serializer):
    """Serializer to define users' log in.
    """

    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)

    def validate(self, data):
        """Define how to check log in credentials.
        """
        try:
            user = user_services.log_in(
                username=data['username'],
                password=data['password']
            )
        except ValidationError as e:
            raise DRFValidationError(e)
        self.context['user'] = user
        return data

    def create(self, data):
        """Get or create token after credentials validations.
        """
        user = self.context['user']
        token, created = Token.objects.get_or_create(user=user)
        return user, token.key
