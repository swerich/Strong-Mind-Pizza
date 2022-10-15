from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from pizzas.models import Pizza, Topping


# Create your views here.
class PizzaListView(ListView):
    model = Pizza 
    template_name = "pizzas/pizza_list.html"
    
class CreatePizzaView(CreateView):
    model = Pizza 
    template_name = "pizzas/create_pizza.html"
    fields = ["name", "toppings"]
    success_url = '/pizzas/'
    
class UpdatePizzaView(UpdateView):
    model = Pizza 
    template_name = "pizzas/update_pizza.html"
    fields = ["name", "toppings"]
    success_url = '/pizzas/'
    
class DeletePizzaView(DeleteView):
    model = Pizza
    success_url = '/pizzas/'
    
class ToppingListView(ListView):
    model = Topping
    template_name = "pizzas/toppings_list.html"
    
class CreateToppingView(CreateView):
    model = Topping 
    template_name = "pizzas/create_topping.html"
    fields = ["name"]
    success_url = '/pizzas/toppings/'
    
class UpdateToppingView(UpdateView):
    model = Topping 
    template_name = "pizzas/update_topping.html"
    fields = ["name"]
    success_url = '/pizzas/toppings/'
    
class DeleteToppingView(DeleteView):
    model = Topping
    success_url = '/pizzas/toppings/'