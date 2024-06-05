# accounts/forms.py

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm


class UserCreationForm(BaseUserCreationForm):
    """A form for creating new users.
    Includes username, email,
    plus a repeated password."""

    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = BaseUserCreationForm.Meta.fields + ("email",)


class UserChangeForm(BaseUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)
