from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Trip, Note
from django.urls import reverse_lazy

# Create your views here.


def trip_list(request):
    trips = Trip.objects.filter(owner=request.user)
    context = {
        'trips': trips
    }
    return render(request, 'trips/Trip_list.html', context)


class TripCreateView(CreateView):
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']
    #template named model_form.html

    def form_valid(self, form):
        #owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)
