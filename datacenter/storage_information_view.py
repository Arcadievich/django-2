from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.time_formatting_functions import format_duration


def storage_information_view(request):
    non_closed_visits = []
    unfinished_visits = Visit.objects.filter(leaved_at=None)

    for visit in unfinished_visits:
        visit_info = {}
        visit_info['who_entered'] = visit.passcard.owner_name
        visit_info['entered_at'] = visit.entered_at
        visit_duration = visit.get_duration()
        visit_info['duration'] = format_duration(visit_duration)
        non_closed_visits.append(visit_info)
    
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
