from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    client_number = models.CharField(max_length=13)
    client_e_mail = models.EmailField( max_length=254)
    socials = models.URLField(max_length=200)
    address = models.CharField(max_length=50)
    note = models.CharField(max_length=50)

class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    manufacturer_number = models.CharField(max_length=13)
    manufacturer_address = models.CharField(max_length=50)
    manufacturer_site = models.URLField(max_length=200)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='all_records')
    fabric = models.CharField(max_length=50)

class Order(models.Model):
    ordered_product = models.ManyToManyField(Product,related_name='all_records')
    date = models.DateTimeField(auto_now_add=True)
    order_price = Product.objects.aggregate(Sum("price"))
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='all_records')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_records')