from django.shortcuts import render
from django.views.generic import ListView
from .models import Trip, Note

# Create your views here.


def trip_list(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'trips/Trip_list.html', context)


