from django.urls import path
from hindus.menu.views import LocationMenuView

app_name = 'menu'

urlpatterns = [
    path('<trailer_id>/menu', LocationMenuView.as_view(), name='trailer'),
]
