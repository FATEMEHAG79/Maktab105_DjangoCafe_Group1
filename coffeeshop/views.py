from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView, ListView, CreateView
from .models import User, MenuItems, Order, OrderItem
from django.contrib.auth.decorators import login_required
# Create your views here.


class ProfileView(DetailView,LoginRequiredMixin):
    model = User
    template_name = 'profile.html'
    context_object_name = 'users'
    login_url = 'login'


class Changeinformation(UpdateView):
    model = User
    fields = ['username', 'phone_number']
    template_name = 'changeinformation.html'
    success_url = reverse_lazy('profile')


class MenuItemsView(ListView):
    model = MenuItems
    template_name = 'Order_list.html'
    context_object_name = 'menu_items'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(completed=False)


class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'create_order_item.html'
    fields = ['menuitem', 'quantity']
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.order = Order.objects.get(id=self.kwargs['order_id'])
        return super().form_valid(form)
