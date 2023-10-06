from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length="100")
    description = models.TextField()
    price = models.DecimalField()
    
class User(models.Model):
    name = models.CharField(max_length="100")
    email = models.CharField(max_length="100")
    password = models.CharField(max_length="100")
    address = models.TextField()
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField