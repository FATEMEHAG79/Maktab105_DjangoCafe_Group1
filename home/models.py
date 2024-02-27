from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cover')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cover')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='MenuItems')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    menuitem = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    # one_to_one relation with reciept-order-item # noqa


class Order(models.Model):
    orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE) # noqa
    status = models.BooleanField(default=True)
    creat_time = models.DateField(auto_now_add=True, editable=False)
    update_time = models.DateField(auto_now=True, editable=False)
    # one-to-many relation with user



class User(models.Model):
    Contact_us=models.ForeignKey(Contact_us, on_delete=models.CASCADE)
    id=models.IntegerField(Primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number=models.PhoneNumberField((""),unique=True)
    email=models.EmailField(unique=True)
    password=models.AutoField(max_length=20,min_length=8 ,unique=True)
    username=models.CharField(max_length=50 ,min_length=8,unique=True)
    adress=models.CharField()
    #Comments=models.ForeignKey(Comments,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


    class Meta():
        pass



# class Contact_us(models.Model):
#     id=models.IntegerField(max_length=20,unique=True)
#     full_name=models.CharField(max_length=50)
#     email=models.EmailField(unique=True)
#     phone_number=models.PhoneNumberField((""),unique=True)
#     #Comments=models.ForeignKey(Comments,on_delete=models.CASCADE)
    
#     def __str__(self):
#         return self.name

#     class Meta():
#         pass



class Comments(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    text=models.CharField(max_length=150)
    date_text=models.DateTimeField()
    MenuItem=models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    class Meta():
        pass





    


