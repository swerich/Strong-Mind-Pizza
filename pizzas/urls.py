from django.urls import path

from pizzas.views import (
    PizzaListView,
)

urlpatterns = [
    path("", PizzaListView.as_view(), name="pizzas_list"),
]