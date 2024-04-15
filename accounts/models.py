"""
null is database-related. It will be translated to NULL on the database.
blank is validation-related, if blank=True then the field will not be required.
In practice, null and blank are commonly used together in this fashion so that a form allows an
empty value and the database stores that value as NULL.
For string-based fields, you should just use blank=True and not null=True.
"""
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Default user model for the project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe.
    # also, we do not want to have user first and last name
    # unless it is necessary later for certification.
    name = models.CharField(blank=True, max_length=255)
