from django.urls import path
from hindus.menu.views import trailer_menu_view_today, trailer_menu_view_history

app_name = 'menu'

urlpatterns = [
    path('<int:trailer_id>/', trailer_menu_view_today, name='trailer_menu_today'),
    path('<int:trailer_id>/<date_str>/', trailer_menu_view_history, name='trailer_menu_history'),
]
