from django.db import models
from django.conf import settings


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Chef(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
class Pizza(models.Model):
    name = models.CharField(max_length=50, unique=True)
    toppings = models.ManyToManyField(
        'Topping',
        related_name='pizza',
    )
    
    def __str__(self):
        return self.name
    
class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name