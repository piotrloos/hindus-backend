from django.contrib import admin
from hindus.dishes.models import Dish


class DishAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'description_pol',
        'spicy',
        'picture_file',
        'is_vegetarian',
        'order',
    ]
    list_filter = [
        'spicy',
        'is_vegetarian',
    ]
    search_fields = [
        'name',
        'description_pol',
        'description_eng',
    ]


admin.site.register(Dish, DishAdmin)
