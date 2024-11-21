from django.db import models

class Subscriber(models.Model):
    """
    Represents a user subscribed to the mailing list.
    """
    email = models.EmailField(unique=True)  # Ensures email addresses are unique
    subscribed_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the user subscribed

    def __str__(self):
        return self.email