from django.urls import path
from hindus.locations.views import LocationListView, LocationMenuView

app_name = 'locations'

urlpatterns = [
    path('', LocationListView.as_view(), name='list'),
]
