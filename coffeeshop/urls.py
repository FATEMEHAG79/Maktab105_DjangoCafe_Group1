from django.urls import path
from django.views.generic import TemplateView
from . import views
from .views import AboutView,add_to_cart,checkout,update_cart

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='coffeeshop'),
    path('about/', AboutView.as_view(), name='about'),
    path('itemdetail/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('add-to-cart/', add_to_cart, name='add-to-cart'),
    path('checkout/', checkout, name="checkout"),
    path('update-cart/', update_cart, name='update-cart')
]
