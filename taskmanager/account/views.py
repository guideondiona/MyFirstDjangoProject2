from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from account.forms import UserLoginForm, UserRegisterForm


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('main:home')


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy('main:home')