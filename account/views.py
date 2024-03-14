from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.views import LoginView as _LoginView, RedirectURLMixin, LogoutView as _LogoutView
from django.urls import reverse_lazy
from django.views import generic, View
from django.forms import Form
from django.contrib.auth import get_user_model, authenticate, login, logout
from account.models import *
from django.contrib import messages
from .models import User
from django.contrib.auth import login, authenticate, logout


# Create your views here.
# html address must change

class LoginView(_LoginView):
    redirect_authenticated_user = True
    next_page = reverse_lazy("coffeeshop")
    template_name = "login.html"
    model = User

    def form_valid(self, form):
        result = super().form_valid(form)
        return result


# html address must change
class RegisterView(generic.CreateView):
    template_name = "register.html"
    model = User
    fields = ['username','first_name', 'last_name', 'phone_number', 'password', 'email', 'address']
    success_url = reverse_lazy('coffeeshop')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = "/"

    def get(self, request, *args, **kwargs):
        logout(request)

        messages.info(self.request, "Bye Bye 👋🏻")
        return super().get(self.request, *args, **kwargs)


class ProfileView(DetailView, LoginRequiredMixin):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = context['users']
        raw_password = user.check_password('')
        context['raw_password'] = raw_password
        return context


class ChangeinformationView(UpdateView):
    model = User
    fields = ['username', 'phone_number', 'address']
    template_name = 'changeinformation.html'
    success_url = reverse_lazy('coffeeshop')


class PasswordResetCofirmView:
    pass


class ChangePasswordView(PasswordResetConfirmView):
    template_name = "change_password.html"
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('password_reset_complete')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return super().form_valid(form)

    def form_valid(self, form):
        return redirect(self.get_success_url())

    def form_invalid(self, form):
        # This method is called when invalid form data has been POSTed.
        return self.render_to_response(self.get_context_data(form=form))
