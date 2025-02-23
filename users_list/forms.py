from django.contrib.auth.forms import UserCreationForm
from users_list.models import Users


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ("email", "password1", "password2")
