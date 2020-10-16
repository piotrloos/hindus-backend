from django.urls import path
from hindus.locations.views import LocationListView, locations_init_view

app_name = 'locations'

urlpatterns = [
    path('', LocationListView.as_view(), name='list'),
    path('init', locations_init_view, name='init'),
]
