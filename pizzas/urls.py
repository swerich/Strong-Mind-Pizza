from django.urls import path

from pizzas.views import (
    PizzaListView,
    CreatePizzaView,
    UpdatePizzaView,
    DeletePizzaView,
    ToppingListView,
    CreateToppingView,
)

urlpatterns = [
    path("", PizzaListView.as_view(), name="pizzas_list"),
    path("create/", CreatePizzaView.as_view(), name="create_pizza"),
    path("update/<int:pk>", UpdatePizzaView.as_view(), name="update_pizza"),
    path("delete/<int:pk>", DeletePizzaView.as_view(), name="delete_pizza"),
    
    path("toppings/", ToppingListView.as_view(), name="toppings_list"),
    path("toppings/create/", CreateToppingView.as_view(), name="create_topping"),





]