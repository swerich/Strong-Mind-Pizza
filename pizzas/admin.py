from django.contrib import admin
from pizzas.models import Pizza, Topping, Store, Chef


# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    pass


class ToppingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Store)
admin.site.register(Chef)
