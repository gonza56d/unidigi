"""Project URLs."""

# Django
from django.contrib import admin
from django.urls import include, path


# Versioning API URLs
v1_urls = [
    path('users/', include(('unidigi.users.urls', 'users'), namespace='users')),
]

# API's root URLs
api_urls = [
    path('v1/', include(v1_urls)),
]

# Project's root URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls)),
]
