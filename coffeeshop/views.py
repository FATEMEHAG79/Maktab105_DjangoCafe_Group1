from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView
from .models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'


