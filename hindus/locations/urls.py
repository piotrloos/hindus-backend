from django.urls import path
from hindus.locations.views import LocationListView, LocationMenuView, trailers_init_view

app_name = 'locations'

urlpatterns = [
    path('', LocationListView.as_view(), name='list'),
    path('<location>/menu', LocationMenuView.as_view(), name='menu'),
    path('init', trailers_init_view, name='init'),
]
