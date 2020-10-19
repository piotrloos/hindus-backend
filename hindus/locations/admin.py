from django.contrib import admin
from hindus.locations.models import Location, City, DailyMenu

admin.site.register(Location)
admin.site.register(City)
admin.site.register(DailyMenu)
