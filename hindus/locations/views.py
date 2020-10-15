from django.shortcuts import render
from hindus.locations.models import Location, City
from hindus.locations.locations_init import LOCATIONS_INIT


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
