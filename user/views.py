from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import LoginForm

class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'login.html'