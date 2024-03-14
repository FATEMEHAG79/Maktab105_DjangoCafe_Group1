from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, \
    PasswordResetConfirmView
from django.urls import path

from .views import LoginView, LogoutView, RegisterView, ChangeinformationView, ProfileView, ChangePasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', RegisterView.as_view(), name="signup"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('changeinformations/<int:pk>/', ChangeinformationView.as_view(), name="change"),

    path('reset_password/', PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='email_sent.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='reset_pass_to_home.html'),
         name='password_reset_complete')
]
