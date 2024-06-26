from django.urls import path
from .views import trip_list, TripCreateView, TripDetailView, NoteDetailView, NoteListView, home_page

urlpatterns = [
    path('', home_page),
    path('dashboard/', trip_list, name='trip-list'),
    path('dashboard/notes/', NoteListView.as_view(), name='note-list'),
    path('dashboard/trip/create/', TripCreateView.as_view(), name='trip-create'),
    path('dashboard/trip/<int:pk>/', TripDetailView.as_view(), name='trip-detail'),
    path('dashboard/note/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
]
