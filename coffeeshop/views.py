import json

from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView
from django.http import JsonResponse
from .models import MenuItems, Order, OrderItem, Order


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

class ItemDetailView(DetailView):
    model = 'MenuItems'
    template_name = 'ItemDetailView.html'
    def get(self,request, pk):
        item=get_object_or_404(MenuItems, pk=pk)
        return render(request,"ItemDetailView.html",{"item":item})


def add_to_cart(request):
    current_user = request.user
    if request.method == "POST":
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            # print('injaaaaa hastamm   product_id', product_id)
            product_check = MenuItems.objects.get(id=product_id)
            if product_check:
                if Order.objects.filter(user=current_user, product_id=product_id):
                    return JsonResponse({'status': 'Product is Already in Cart'})
                else:
                    product_qyt = 1
                    Order.objects.create(user=current_user, product_id=product_id, quantity=product_qyt)
                    return JsonResponse({'status': 'Product added successfuly'})
            else:
                return JsonResponse({'status': 'No such Product found'})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')
def checkout(request):
    context = {}
    cart_items = Order.objects.filter(user=request.user)

    context['cart_items'] = cart_items
    context['cart_total'] = cart_items.count()

    cart_total = 0
    total_price = 0
    if cart_items:
        for item in cart_items:
            total_price += (item.product.price) * item.quantity
            cart_total += item.quantity

        context['total_price'] = total_price
        context['cart_total'] = cart_total

    return render(request, 'checkout.html', context)


def update_cart(requset):
    data = json.loads(requset.body)
    prod_id = data['productId']
    action = data['action']

    cart_item = Order.objects.filter(user=requset.user, product_id=prod_id)[0]

    if cart_item:
        if action == 'add':
            cart_item.quantity += 1
        elif action == 'remove':
            cart_item.quantity -= 1

        cart_item.save()

        if cart_item.quantity == 0:
            cart_item.delete()

    return JsonResponse({'status': "Update Successfully"})