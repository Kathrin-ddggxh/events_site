from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import UpcomingEvent
from .forms import EventForm


class UpcomingEvents(ListView):
    """
    renders upcoming events on events page
    """

    template_name = "events/upcoming.html"
    model = UpcomingEvent
    context_object_name = "events"


class AddEvent(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "events/add_event.html"
    model = UpcomingEvent
    form_class = EventForm
    success_url = "/events/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)
