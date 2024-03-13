"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.coffeeshop, name='coffeeshop')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='coffeeshop')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from account.views import *
from coffeeshop.views import MenuItemsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("coffeeshop.urls")),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('account/',include("account.url")),
    path('menu/', MenuItemsView.as_view(), name='menu_items'),
    path('reserv/',include('reservation.url'))
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)