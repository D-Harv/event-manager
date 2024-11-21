from django.db import models
from django.utils.timezone import now

class Event(models.Model):
    """
    Represents an event that users can RSVP to.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    max_slots = models.PositiveIntegerField()  # Total available slots
    slots_filled = models.PositiveIntegerField(default=0)  # Number of slots already taken
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)  # Event image
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the event was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update

    def slots_available(self):
        """
        Returns the number of slots still available for the event.
        """
        return self.max_slots - self.slots_filled

    def is_full(self):
        """
        Returns True if the event is fully booked, False otherwise.
        """
        return self.slots_available() <= 0

    def __str__(self):
        return self.title