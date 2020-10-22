from django.shortcuts import render
from django.views.generic import ListView  # , UpdateView
from hindus.locations.models import Trailer
from hindus.locations.locations_init import TRAILERS_INIT
from hindus.menu.models import TrailerMenu


class LocationListView(ListView):
    model = Trailer
    template_name = 'trailers_list.html'
    context_object_name = 'trailers'
    ordering = 'order'

    # def get_queryset(self):
    #     return super().get_queryset().filter(serving_date=date.today())


class LocationMenuView(ListView):
    model = TrailerMenu
    template_name = 'locations_list.html'
    context_object_name = 'locations'


def trailers_init_view(request):

    Trailer.objects.all().delete()
    print("Deleted all Trailers objects in database.")

    for trailer_init in TRAILERS_INIT:

        trailer = Trailer()
        for key, value in trailer_init.items():
            trailer.__setattr__(key, value)

        trailer.save()
        print("Saved object {trailer} to database.".format(trailer=trailer))

    query_results = Trailer.objects.all()
    return render(request, template_name="locations_list.html", context={'locations': query_results})

#
# class DailyMenuUpdateView(UpdateView):
#     model = DailyMenu
#     fields = ['serving_date']
#     template_name = 'dailymenu_form.html'
