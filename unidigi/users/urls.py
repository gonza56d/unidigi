"""Users URLs."""

# Django
from django.urls import include, path

# DRF
from rest_framework.routers import DefaultRouter

# Unidigi
from .api.viewsets import UserViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]
