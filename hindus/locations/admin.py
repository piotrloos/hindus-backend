from django.contrib import admin
from hindus.locations.models import City, Trailer, Foodtruck


class CityAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'order',
    ]
    search_fields = [
        'name',
    ]


class TrailerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'city',
        'open_hours_workday',
        'open_hours_saturday',
        'open_hours_sunday',
        'address',
        'telephone',
        'order',
    ]
    list_filter = [
        'city',
    ]
    search_fields = [
        'name',
        'city',
        'address',
    ]


class FoodtruckAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'id',
        'city',
        'open_hours_workday',
        'open_hours_saturday',
        'open_hours_sunday',
        'address',
        'telephone',
        'order',
    ]
    list_filter = [
        'city',
    ]
    search_fields = [
        'name',
        'city',
        'address',
    ]


admin.site.register(City, CityAdmin)
admin.site.register(Trailer, TrailerAdmin)
admin.site.register(Foodtruck, FoodtruckAdmin)
