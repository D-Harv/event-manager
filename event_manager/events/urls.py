from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Homepage showing all events
    path('<int:event_id>/', views.event_detail, name='event_detail'),  # Detail view for a specific event
    path('<int:event_id>/rsvp/', views.rsvp, name='rsvp'),  # RSVP endpoint for an event
]