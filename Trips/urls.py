from django.urls import path
from .views import trip_list, TripCreateView
urlpatterns = [
    path('dashboard/', trip_list, name='trip-list'),
    path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create'),
]
