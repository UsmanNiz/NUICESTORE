from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    def __str__(self):
        return self.name
class Sign(models.Model):
    username = models.CharField(max_length=70, primary_key=True)
    password = models.CharField(max_length=70, default="00000000")
    name = models.CharField(max_length=10, default="abc")
    def __str__(self):
        return self.username
#class Come(models.Model):
#    c_id = models.AutoField(primary_key = True)
#    name = models.CharField(max_length=50)
#    email = models.CharField(max_length=70, default="")
#    phone = models.CharField(max_length=70, default="")
#class History(models.Model):
    #dictionary containing all the sold products_id(Fkey),date,price,c_id(foreign key)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()