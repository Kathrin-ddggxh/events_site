from django.urls import path
from .views import UpcomingEvents, AddEvent


urlpatterns = [
    path("add/", AddEvent.as_view(), name="add_event"),
    path("", UpcomingEvents.as_view(), name="upcoming"),
]
