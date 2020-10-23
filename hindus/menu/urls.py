from django.urls import path
from hindus.menu.views import LocationMenuView

app_name = 'menu'

urlpatterns = [
    path('<int:trailer_id>/', LocationMenuView.as_view(), name='trailer'),
]
