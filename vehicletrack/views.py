from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Vehicle, NavigationRecord
from datetime import datetime, timedelta

def index(request):
    last48hours = NavigationRecord.objects.filter(datetime__gte=datetime.now() - timedelta(hours = 48))
    print(last48hours)
    template = loader.get_template('vehicletrack/index.html')
    context = {
        'last48hours': last48hours,
    }
    return HttpResponse(template.render(context, request))


def vehicledetail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)


def navresults(request, nav_id):
    response = "You're looking at the results of navigation %s."
    return HttpResponse(response % nav_id)
