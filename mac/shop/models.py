from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django import forms
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
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=70, default="00000000")
    name = models.CharField(max_length=40, default="")
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.username
# <<<<<<< HEAD
class SignIn(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    username = models.CharField(max_length=25 , primary_key=True)
    password = models.CharField(max_length=70, default="00000000")

class Cart(models.Model):
    cart_id = models.CharField(max_length=25,primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

class Invoice (models.Model):
    invoice_id = models.AutoField( primary_key= True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)


class Feedback(models.Model):
    choice = (
        (1),(2),(3),(4),(5)
    )
    feedback_id = models.AutoField( primary_key= True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = forms.ChoiceField(choices = choice)

class History(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)

# class User(Sign):
#     is_email_verified = models.BooleanField(default=False)
#


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # bio = models.TextField(max_length=500, blank=True)
#     # location = models.CharField(max_length=30, blank=True)
#     # birth_date = models.DateField(null=True, blank=True)
#     email_confirmed = models.BooleanField(default=False)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
# class User(Sign):
#     is_email_verified = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.email

# class Come(models.Model):
    #    c_id = models.AutoField(primary_key = True)
    #    name = models.CharField(max_length=50)
    #    email = models.CharField(max_length=70, default="")
    #    phone = models.CharField(max_length=70, default="")

# class History(models.Model):
    # dictionary containing all the sold products_id(Fkey),date,price,c_id(foreign key)

# =======
#class Come(models.Model):
#    c_id = models.AutoField(primary_key = True)
#    name = models.CharField(max_length=50)
#    email = models.CharField(max_length=70, default="")
#    phone = models.CharField(max_length=70, default="")
#class History(models.Model):
    #dictionary containing all the sold products_id(Fkey),date,price,c_id(foreign key)


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
#     email_confirmed = models.BooleanField(default=False)
#
#
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
# class User(Sign):
#     is_email_verified = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.email
# >>>>>>> 255f6d868542df49ce5e52f76d1e34367a673d89
