from django.contrib import admin
from .models import *
admin.site.register(Category)
admin.site.register(User)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Table)
admin.site.register(MenuItems)

