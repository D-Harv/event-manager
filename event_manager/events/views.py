from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendee
from .forms import RSVPForm

def event_list(request):
    """
    Displays a list of all events with availability information.
    """
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = RSVPForm(request.POST, event=event)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event

            # Decrement the slot count for the selected profession
            profession = attendee.profession
            current_slots = getattr(event, f"{profession}_slots")
            setattr(event, f"{profession}_slots", current_slots - 1)
            event.sagit ve()

            attendee.save()
            return render(request, 'rsvp_success.html', {'event': event})
    else:
        form = RSVPForm(event=event)
    return render(request, 'event_detail.html', {'event': event, 'form': form})



def rsvp(request, event_id):
    """
    Handles RSVP form submissions for a specific event.
    """
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = RSVPForm(request.POST, event=event)
        if form.is_valid():
            attendee = form.save(commit=False)
            attendee.event = event

            # Decrement the slot count for the selected profession
            profession = attendee.profession
            current_slots = getattr(event, f"{profession}_slots")
            setattr(event, f"{profession}_slots", current_slots - 1)
            event.save()

            attendee.save()
            return render(request, 'events/rsvp_success.html', {'event': event})
    else:
        form = RSVPForm(event=event)

    return render(request, 'event_rsvp.html', {'event': event, 'form': form})