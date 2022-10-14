from django.urls import path

from pizzas.views import (
    PizzaListView,
    CreatePizzaView,
    UpdatePizzaView
)

urlpatterns = [
    path("", PizzaListView.as_view(), name="pizzas_list"),
    path("create/", CreatePizzaView.as_view(), name="create_pizza"),
    path("update/<int:pk>", UpdatePizzaView.as_view(), name="update_pizza"),


]