from django.db import models
from account.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='media', unique=True, null=True)
    # parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='MenuItems')
    def get_absolute_url(self):
        return reverse("item_detail",args=[self.id])
    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField()
    is_reserved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="table")


class Order(models.Model):
    completed = models.BooleanField(default=False)
    ordered_at = models.DateField(auto_now_add=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)


class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=150)
    date_text = models.DateTimeField()
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)

    def __str__(self):
        return (
            f"User: {self.user}, "
            f"Title: {self.title}, "
            f"Text: {self.text}, "
            f"Date: {self.date_text}, "
            f"Menu Item: {self.menu_item}"
        )
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product.name