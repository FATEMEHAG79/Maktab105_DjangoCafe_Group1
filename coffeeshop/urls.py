from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import AboutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='coffeeshop'),
    path('about/', AboutView.as_view(), name='about'),
    path('itemdetail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
]
