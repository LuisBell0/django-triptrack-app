from django.urls import path
from .views import trip_list

urlpatterns = [
    path('', trip_list, name='trip-list')
]
