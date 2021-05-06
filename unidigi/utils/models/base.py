# Django
from django.db import models


class BaseModel(models.Model):
    """Base model that adds utility fields such as time created and last time
    modified. Provides also ordering defaults.
    """

    created = models.DateTimeField(
        'date and time when created',
        auto_now=True
    )

    modified = models.DateTimeField(
        'date and time when last modified',
        auto_now_add=True
    )

    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']
