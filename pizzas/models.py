from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)

class Chef(models.Model):
    name = models.CharField(max_length=50)
    
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