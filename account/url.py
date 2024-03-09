from django.urls import path
from .views import LoginView,LogoutView,RegisterView
from coffeeshop.views import ProfileView
from coffeeshop.views import ChangeinformationView

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',RegisterView.as_view(),name="signup"),
    path('profile/<int:pk>/', ProfileView.as_view(), name="profile"),
    path('changeinformations/<int:pk>/', ChangeinformationView.as_view(), name="change")
]