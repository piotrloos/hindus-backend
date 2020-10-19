from django.urls import path
from hindus.dishes.views import DishListView, DishEditView, dish_init_view

app_name = 'dishes'

urlpatterns = [
    path('', DishListView.as_view(), name='list'),
    path('edit', DishEditView.as_view(), name='edit'),
    path('init', dish_init_view, name='init'),
]
