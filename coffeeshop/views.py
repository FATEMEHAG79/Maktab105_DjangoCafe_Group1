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


class MenuItemsView(ListView):
    model = MenuItems
    template_name = 'menu_items.html'
    context_object_name = 'menu_items'

    def get_queryset(self):
        return MenuItems.objects.all()


class OrderListView(ListView):
    model = Order
    template_name = 'order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(completed=False)


class OrderItemCreateView(CreateView):
    model = OrderItem
    template_name = 'orderitem.html'
    fields = ['menuitem', 'quantity']
    success_url = reverse_lazy('order_list')

    def form_valid(self, form):
        form.instance.order = Order.objects.get(id=self.kwargs['order_id'])
        return super().form_valid(form)

class AboutView(TemplateView):
    template_name = 'About.html'


class HistoryView(ListView):
    model=Order
    template_name='donecart.html'  
    def filtter_type():
        order_history= Order.objects.filter(user='username').values()
        return order_history
    

    