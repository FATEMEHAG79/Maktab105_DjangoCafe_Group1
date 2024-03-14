from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class reservation(models.Model):
    name=models.CharField(_("name"),max_length=200)
    email=models.EmailField(_("email"),max_length=254)
    phone=models.CharField(_('phone'),max_length=20)
    number=models.IntegerField(_('number'))
    date=models.DateField(_("date"),auto_now=False,auto_now_add=False)
    date=models.TimeField(_("time"),auto_now=False,auto_now_add=False)

    def __str__(self) -> str:
        return self.email
    
    