from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from datetime import date
from hindus.locations.models import Trailer


def trailer_menu_view(request, trailer_id, serving_date):

    trailer = get_object_or_404(Trailer, pk=trailer_id)

    qs = trailer.menu.filter(serving_date=serving_date)
    # qs = TrailerMenu.objects.filter(trailer=trailer).get(serving_date=serving_date)

    template_name = 'menu_list.html'
    context = {
        'serving_date': serving_date,
        'trailer_name': trailer.name,
    }

    if len(qs):
        context['dishes'] = qs[0].dishes.values()

    return render(request, template_name, context)


def trailer_menu_view_today(request, trailer_id):

    return trailer_menu_view(request, trailer_id, date.today())


def trailer_menu_view_history(request, trailer_id, date_str):

    try:
        serving_date = date.fromisoformat(date_str)
    except ValueError:
        raise Http404

    return trailer_menu_view(request, trailer_id, serving_date)
