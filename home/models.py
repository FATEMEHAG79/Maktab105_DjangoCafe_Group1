from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cover')
    # parent = models.ForeignKey('self',related_name='children',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class MenuItems(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='cover')
    category = models.ForeignKey(Category,on_delete = models.PROTECT,related_name='MenuItems')
    def __str__(self):
        return self.name
