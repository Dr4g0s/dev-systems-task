from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'birthdate')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('phone_number', 'first_name', 'last_name', 'birthdate')
