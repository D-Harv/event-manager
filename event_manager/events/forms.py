from django import forms
from .models import Attendee

class RSVPForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = ['email', 'first_name', 'profession']
        widgets = {
            'profession': forms.Select(choices=Attendee.PROFESSIONS),
        }

    def __init__(self, *args, **kwargs):
        self.event = kwargs.pop('event')  # Pass the event object to the form
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        profession = cleaned_data.get('profession')

        # Check if the user has already RSVP'd for this event
        if Attendee.objects.filter(event=self.event, email=email).exists():
            raise forms.ValidationError("You have already RSVP'd for this event.")

        # Check if there are available slots for the selected profession
        available_slots = getattr(self.event, f"{profession}_slots")
        if available_slots <= 0:
            raise forms.ValidationError(f"No slots available for {profession}s.")
        
        return cleaned_data