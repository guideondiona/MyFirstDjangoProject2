from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    ...


class UserRegisterForm(UserCreationForm):
    ...