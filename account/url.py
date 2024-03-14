from django.urls import path

from .views import LoginView, LogoutView, RegisterView, ChangeinformationView, ProfileView, ChangePasswordView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',RegisterView.as_view(),name="signup"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('changeinformations/<int:pk>/', ChangeinformationView.as_view(), name="change")
]