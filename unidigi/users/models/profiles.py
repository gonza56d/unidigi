# Django
from django.db import models

# Project
from unidigi.utils.models import BaseModel, CommonRegex


class Profile(BaseModel):
    """User profiles model.
    """

    class Roles(models.TextChoices):
        TEACHER = 'T', 'Teacher'
        STUDENT = 'S', 'Student'

    role = models.CharField(
        'profile role type',
        max_length=1,
        choices=Roles.choices
    )

    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    first_name = models.CharField(
        "user's first names",
        max_length=100, validators=[CommonRegex.LETTERS]
    )

    last_name = models.CharField(
        "user's last names",
        max_length=100, validators=[CommonRegex.LETTERS]
    )

    birthday = models.DateField(
        "user's birthday",
        null=True, blank=True
    )

    picture = models.ImageField(
        "user's profile picture",
        upload_to='profiles', blank=True
    )
