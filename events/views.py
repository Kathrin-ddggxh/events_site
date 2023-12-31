from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import UpcomingEvent
from .forms import EventForm


class UpcomingEvents(ListView):
    """
    renders upcoming events on events page
    """

    template_name = "events/upcoming.html"
    model = UpcomingEvent
    queryset = UpcomingEvent.objects.order_by('datetime')
    context_object_name = "events"


class AddEvent(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Add recipe view"""

    template_name = "events/add_event.html"
    model = UpcomingEvent
    form_class = EventForm
    success_url = "/events/"
    success_message = "New event was added successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEvent, self).form_valid(form)
