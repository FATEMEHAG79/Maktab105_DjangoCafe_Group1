from django.shortcuts import render
from django.contrib.auth.views import LoginView as _LoginView, RedirectURLMixin , LogoutView as _LogoutView
from django.urls import reverse_lazy
from django.views import generic, View
from django.forms import Form
from django.contrib.auth import get_user_model, authenticate, login, logout
from account.models import *
from django.contrib import messages
from .models import User



# Create your views here.
#html address must change

class LoginView(_LoginView):
    redirect_authenticated_user = True
    next_page = reverse_lazy("contact")
    template_name = "login.html"
    model = User

    def form_valid(self, form):
        result = super().form_valid(form)
        return result
    
#html address must change
class RegisterView(generic.CreateView):
    template_name = "auth/register.html"
    model = User
    fields = ['first_name', 'last_name', 'phone_number', 'password','email','address']
    success_url = "/login"

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)    


class LogoutView(_LogoutView):
    # redirect_authenticated_user=False
    # next_page="landing:login"
    # template_name="auth/logout.html"
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)

        messages.info(self.request, "Bye Bye 👋🏻")
        return super().get(self.request, *args, **kwargs)

