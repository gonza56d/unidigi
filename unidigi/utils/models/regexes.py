"""Common regexes."""

# Django
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class CommonRegex:
    """Common regular expression validations.
    """

    LOWERCASE_AND_NUMBERS = RegexValidator(
        regex='[a0-z9]',
        message=_('Only lowercase letters and numbers allowed')
    )
    LETTERS_AND_NUMBERS = RegexValidator(
        regex='[aA0-zA9]',
        message=_('Only letters and numbers allowed')
    )
    LETTERS = RegexValidator(
        regex='[aA-zZ]',
        message=_('Only letters allowed')
    )
    LOWERCASE = RegexValidator(
        regex='[a-z]',
        message=_('Only lowercase letters allowed')
    )
