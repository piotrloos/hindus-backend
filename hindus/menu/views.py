from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from hindus.menu.models import Dish
from hindus.menu.menu_init import MENU_INIT


class MenuListView(ListView):
    model = Dish
    template_name = 'menu_list.html'
    context_object_name = 'dishes'
    ordering = 'order'

    def get_queryset(self):
        return super().get_queryset().filter(is_cooked_today=True)


class MenuEditView(ListView):
    model = Dish
    template_name = 'menu_list.html'
    context_object_name = 'dishes'
    ordering = 'order'


def menu_init_view(request):

    Dish.objects.all().delete()
    print("Deleted all objects in database.")

    for dish_init in MENU_INIT:

        dish = Dish()

        dish.order = dish_init[0]
        dish.name = dish_init[1]
        dish.spicy = dish_init[2]
        dish.description_pol = dish_init[3]
        dish.description_eng = dish_init[4]
        dish.picture_file = dish_init[5]
        dish.is_vegetarian = dish_init[6]
        dish.is_cooked_today = False

        dish.save()
        print("Saved object {dish} to database.".format(dish=dish))

    query_results = Dish.objects.all()
    return render(request, template_name="menu_list.html", context={'dishes': query_results})


def menu_switch(request, pk):
    dish = Dish.objects.get(pk=pk)
    dish.is_cooked_today = not dish.is_cooked_today
    dish.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
