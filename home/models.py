from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager ,BaseUserManager,PermissionsMixin
import uuid
# Create your models here.PermissionsMixin


class Menu(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cover')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    # parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cover')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='MenuItems')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    _MenuItems = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    # one_to_one relation with reciept-order-item # noqa


class Order(models.Model):
    orderitem = models.ForeignKey(OrderItem, on_delete=models.CASCADE) # noqa
    status = models.BooleanField(default=True)
    creat_time = models.DateField(auto_now_add=True, editable=False)
    update_time = models.DateField(auto_now=True, editable=False)
    # one-to-many relation with user


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_sueruser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self.create_user(email, password, **extra_fields)


class UserModel(AbstractUser, PermissionsMixin):
    id               = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)                     
    username         = None
    email            = models.EmailField(unique = True,  null = True)
    first_name       = models.CharField(max_length = 50, null = True)
    last_name        = models.CharField(max_length = 50, null = True)
    created_at       = models.DateTimeField(auto_now_add=True)
    is_confirmEmail  = models.BooleanField(default=False)
    enable_two_factor_authentication = models.BooleanField(null=True, blank=True)
    

    objects = UserManager()

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name"]
   
    def __str__(self):
       return "{}".format(self.email) 
    
    @property
    def get_user_fullname(self):
        return f"{self.first_name} {self.last_name}"
    









class Comments(models.Model):
    User=models.ForeignKey(UserModel,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    text=models.CharField(max_length=150)
    date_text=models.DateTimeField()
    MenuItem=models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
    class Meta():
        pass





    


