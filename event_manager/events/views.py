from django.shortcuts import render, get_object_or_404, redirect
from .models import Event

def event_list(request):
    """
    Displays a list of all events with availability information.
    """
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_detail(request, event_id):
    """
    Displays detailed information about a specific event.
    """
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_detail.html', {'event': event})

def rsvp(request, event_id):
    """
    Allows a user to RSVP for a specific event.
    """
    event = get_object_or_404(Event, id=event_id)
    if not event.is_full():  # Assume `is_full` is a method in the Event model
        event.slots_filled += 1
        event.save()
    return redirect('event_detail', event_id=event_id)
    