from django.urls import path
from hindus.menu.views import MenuListView, menu_init_view, menu_switch

app_name = 'menu'

urlpatterns = [
    path('', MenuListView.as_view(), name='list'),
    path('init', menu_init_view, name='init'),
    path('<int:pk>/switch', menu_switch, name='switch'),
]
