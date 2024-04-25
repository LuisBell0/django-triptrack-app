from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Trip, Note
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_page(request):
    return render(request, 'trips/home_page.html')

@login_required
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
    # template named model_form.html

    def form_valid(self, form):
        # owner field = logged in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    # template: model_detail.html
    # data stored on Trip - also have the notes data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context


class NoteDetailView(DetailView):
    model = Note


class NoteListView(ListView):
    model = Note
    # TEMPLATE: model_list.html
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset
