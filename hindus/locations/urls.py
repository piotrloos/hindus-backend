from django.urls import path
from hindus.locations.views import locations_init_view

app_name = 'locations'

urlpatterns = [
    path('init', locations_init_view, name='init'),
]
