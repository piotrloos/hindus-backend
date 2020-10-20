from django.contrib import admin
from hindus.menu.models import TrailerMenu, FoodtruckMenu


class TrailerMenuAdmin(admin.ModelAdmin):
    list_display = [
        'serving_date',
        'id',
        'trailer',
    ]
    list_filter = [
        'serving_date',
        'trailer',
    ]
    search_fields = [
        # 'trailer',
    ]


class FoodtruckMenuAdmin(admin.ModelAdmin):
    list_display = [
        'serving_date',
        'id',
        'foodtruck',
    ]
    list_filter = [
        'serving_date',
        'foodtruck',
    ]
    search_fields = [
        # 'foodtruck',
    ]


admin.site.register(TrailerMenu, TrailerMenuAdmin)
admin.site.register(FoodtruckMenu, FoodtruckMenuAdmin)
