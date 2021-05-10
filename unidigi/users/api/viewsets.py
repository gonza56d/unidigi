"""Users viewsets."""

# DRF
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response

# Unidigi
from ..models import User
from .serializers import (
    UserSerializer,
    UserSignUpSerializer,
    UserLogInSerializer
)


class UserViewSet(#ListModelMixin,
                  #RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """Viewset for logging in, signing up, listing, retrieving, and updating
    users.
    """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    @action(detail=False, methods=['POST'])
    def sign_up(self, request):
        """Handle users sign up requests.
        """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'])
    def log_in(self, request):
        """Handle users log in requests.
        """
        serializer = UserLogInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.status.HTTP_201_CREATED)
