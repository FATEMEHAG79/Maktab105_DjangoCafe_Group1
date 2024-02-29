from django.db import models


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.PhoneNumberField("", unique=True)
    email = models.EmailField(unique=True)
    password = models.AutoField(max_length=20, min_length=8, unique=True)
    username = models.CharField(max_length=50, min_length=8, unique=True)
    address = models.CharField()

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"Name: {self.first_name} {self.last_name}, "
            f"Phone: {self.phone_number}, "
            f"Email: {self.email}, "
            f"Username: {self.username}, "
            f"Address: {self.address}"
        )

    class Meta:
        pass


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cover')
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_actived = models.BooleanField(default=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cover')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='MenuItems')

    def __str__(self):
        return self.name


class Table(models.Model):
    table_number = models.IntegerField()
    is_reseved = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name="table")


class Order(models.Model):
    complete = models.BooleanField(default=False)
    orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE)  # noqa
    ordered_at = models.DateField(auto_now_add=True, editable=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)


class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.integerField(default=0, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class Comments(models.Model):
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

    class Meta:
        pass
