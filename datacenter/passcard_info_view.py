from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.time_formatting_functions import format_duration


def passcard_info_view(request, passcode):
    requested_passcard = get_object_or_404(Passcard, passcode=passcode)
    individula_visits = Visit.objects.filter(passcard=requested_passcard)

    this_passcard_visits = []

    for visit in individula_visits:
        visit_info = {}
        visit_info['entered_at'] = visit.entered_at
        visit_duration = visit.get_duration()
        visit_info['duration'] = format_duration(visit_duration)
        visit_info['is_strange'] = visit.is_long()
        this_passcard_visits.append(visit_info)


    context = {
        'passcard': requested_passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)