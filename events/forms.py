from django import forms
from .models import UpcomingEvent


class EventForm(forms.ModelForm):
    """
    Form to create new upcoming event
    """

    class Meta:
        model = UpcomingEvent
        fields = [
            "location",
            "venue",
            "datetime",
            "admission",
            "max_tickets",
            "cancelled",
        ]

        widgets = {
            "datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }

        labels = {
            "location": "Location",
            "venue": "Venue",
            "datetime": "Choose Date and Time",
            "admission": "Admission Fee",
            "max_tickets": "Maximum Tickets available",
            "cancelled": "Do you want to cancel this event?",
        }
