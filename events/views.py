from django.views.generic import TemplateView


class UpcomingEvents(TemplateView):
    """
    renders events page
    """

    template_name = "events/upcoming.html"