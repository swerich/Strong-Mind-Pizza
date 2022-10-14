from django.urls import path

from pizzas.views import (
    PizzaListView,
    CreatePizzaView,
)

urlpatterns = [
    path("", PizzaListView.as_view(), name="pizzas_list"),
    path("create/", CreatePizzaView.as_view(), name="create_pizza"),

]