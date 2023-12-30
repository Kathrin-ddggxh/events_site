from django.views.generic import ListView

from .models import UpcomingEvent


class UpcomingEvents(ListView):
    """
    renders upcoming events on events page
    """

    template_name = "events/upcoming.html"
    model = UpcomingEvent
    context_object_name = "events"
