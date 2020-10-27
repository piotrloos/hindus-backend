from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import get_object_or_404
from datetime import date
from hindus.locations.models import Trailer


def trailer_menu_view(request, trailer_id, date_str=str(date.today())):

    trailer = get_object_or_404(Trailer, pk=trailer_id)

    try:
        serving_date = date.fromisoformat(date_str)
    except ValueError:
        raise Http404

    qs = trailer.menu.filter(serving_date=serving_date)

    if len(qs) == 0:
        template_name = 'menu_empty.html'
        context = {'serving_date': serving_date, 'trailer_name': trailer.name}
    else:
        template_name = 'menu_list.html'
        context = {'serving_date': serving_date, 'trailer_name': trailer.name, 'dishes': qs[0].dishes.values()}

    return render(request, template_name, context)
