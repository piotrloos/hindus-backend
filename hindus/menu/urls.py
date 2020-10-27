from django.urls import path
from hindus.menu.views import trailer_menu_view

app_name = 'menu'

urlpatterns = [
    path('<int:trailer_id>/', trailer_menu_view, name='trailer_menu_today'),
    path('<int:trailer_id>/<date_str>/', trailer_menu_view, name='trailer_menu'),
]
