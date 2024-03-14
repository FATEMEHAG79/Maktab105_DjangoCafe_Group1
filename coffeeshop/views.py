from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .models import MenuItems, Order, OrderItem


# Create your views here.


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
    model = Order
    template_name = 'donecart.html'

    @staticmethod
    def filter_type():
        order_history = Order.objects.filter(user='username').values()
        return order_history
