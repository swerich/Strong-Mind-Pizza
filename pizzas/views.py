from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView
from pizzas.models import Pizza


# Create your views here.
class PizzaListView(ListView):
    model = Pizza 
    template_name = "pizzas/pizza_list.html"
    
class CreatePizzaView(CreateView):
    model = Pizza 
    template_name = "pizzas/create_pizza.html"
    fields = ["name", "toppings"]
    success_url = '/pizzas/'