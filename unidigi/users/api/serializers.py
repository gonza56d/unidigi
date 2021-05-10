"""Users serializers."""

# DRF
from rest_framework import serializers

# Unidigi
from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer.
    """

    class Meta:
        model = User
        fields = ['username', 'email', 'created', 'profile']
