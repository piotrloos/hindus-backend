from django.shortcuts import render
from django.views.generic import ListView, UpdateView
from datetime import date
from hindus.locations.models import Location, DailyMenu
from hindus.locations.locations_init import LOCATIONS_INIT


class LocationListView(ListView):
    model = Location
    template_name = 'locations_list.html'
    context_object_name = 'locations'
    ordering = 'order'

    def get_queryset(self):
        return super().get_queryset().filter(serving_date=date.today())


def locations_init_view(request):

    Location.objects.all().delete()
    print("Deleted all objects in database.")

    for location_init in LOCATIONS_INIT:

        location = Location()
        for key, value in location_init.items():
            location.__setattr__(key, value)

        location.save()
        print("Saved object {location} to database.".format(location=location))

    query_results = Location.objects.all()
    return render(request, template_name="locations_list.html", context={'locations': query_results})


class DailyMenuUpdateView(UpdateView):
    model = DailyMenu
    fields = ['serving_date']
    template_name = 'dailymenu_form.html'
