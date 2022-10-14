from django.shortcuts import render
from django.views.generic.list import ListView
from pizzas.models import Pizza


# Create your views here.
class PizzaListView(ListView):
    model = Pizza 
    template_name = "pizzas/pizza_list.html"