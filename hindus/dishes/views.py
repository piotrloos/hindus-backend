from django.shortcuts import render
from django.views.generic import ListView
from hindus.dishes.models import Dish
from hindus.dishes.dish_init import DISH_INIT


class DishListView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'
    ordering = 'order'

    # def get_queryset(self):
        # return super().get_queryset().filter(is_vegetarian=True)


class DishEditView(ListView):
    model = Dish
    template_name = 'dish_list.html'
    context_object_name = 'dishes'
    ordering = 'order'


def dish_init_view(request):

    Dish.objects.all().delete()
    print("Deleted all Dish objects in database.")

    for dish_init in DISH_INIT:

        dish = Dish()
        for key, value in dish_init.items():
            dish.__setattr__(key, value)

        dish.save()
        print("Saved object {dish} to database.".format(dish=dish))

    query_results = Dish.objects.all()
    return render(request, template_name="dish_list.html", context={'dishes': query_results})
