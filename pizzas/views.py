from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from pizzas.models import Pizza, Topping
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Authorization


def is_chef(user):
    try:
        user.chef
        return True
    except Exception:
        return False


def is_owner(user):
    try:
        user.store
        return True
    except Exception:
        return False


# Create your views here.
class PizzaListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Pizza
    template_name = "pizzas/pizza_list.html"
    paginate_by = 10

    def test_func(self):
        print("PRINT", self.request.user)
        return is_chef(self.request.user)


class CreatePizzaView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Pizza
    template_name = "pizzas/create_pizza.html"
    fields = ["name", "toppings"]
    success_url = "/pizzas/"

    def test_func(self):
        return is_chef(self.request.user)


class UpdatePizzaView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pizza
    template_name = "pizzas/update_pizza.html"
    fields = ["name", "toppings"]
    success_url = "/pizzas/"

    def test_func(self):
        return is_chef(self.request.user)


class DeletePizzaView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pizza
    success_url = "/pizzas/"

    def test_func(self):
        return is_chef(self.request.user)


class ToppingListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Topping
    template_name = "pizzas/toppings_list.html"
    paginate_by = 10

    def test_func(self):
        return is_owner(self.request.user)


class CreateToppingView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Topping
    template_name = "pizzas/create_topping.html"
    fields = ["name"]
    success_url = "/pizzas/toppings/"

    def test_func(self):
        return is_owner(self.request.user)


class UpdateToppingView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Topping
    template_name = "pizzas/update_topping.html"
    fields = ["name"]
    success_url = "/pizzas/toppings/"

    def test_func(self):
        return is_owner(self.request.user)


class DeleteToppingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topping
    success_url = "/pizzas/toppings/"

    def test_func(self):
        return is_owner(self.request.user)
