from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    max_slots = models.PositiveIntegerField()
    inspector_slots = models.PositiveIntegerField(default=0)
    photographer_slots = models.PositiveIntegerField(default=0)
    contractor_slots = models.PositiveIntegerField(default=0)
    real_estate_slots = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def slots_filled(self):
        """
        Calculate total slots filled across all professions.
        """
        total_reserved = (
            self.max_slots -
            (self.inspector_slots +
             self.photographer_slots +
             self.contractor_slots +
             self.real_estate_slots)
        )
        return total_reserved

    @property
    def slots_available(self):
        """
        Calculate total available slots.
        """
        return self.inspector_slots + self.photographer_slots + self.contractor_slots + self.real_estate_slots

    @property
    def is_full(self):
        """
        Check if the event is fully booked.
        """
        return self.slots_available <= 0

    def __str__(self):
        return self.title


class Attendee(models.Model):
    PROFESSIONS = [
        ('inspector', 'Inspector'),
        ('photographer', 'Photographer'),
        ('contractor', 'Contractor'),
        ('real_estate', 'Real Estate Agent'),
    ]

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendees')
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=20, choices=PROFESSIONS)

    class Meta:
        unique_together = ('event', 'email')  # Prevent duplicate RSVPs for the same event

    def __str__(self):
        return f"{self.first_name} ({self.profession}) - {self.event.title}"