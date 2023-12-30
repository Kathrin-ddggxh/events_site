from django.urls import path
from .views import UpcomingEvents


urlpatterns = [
    path("upcoming", UpcomingEvents.as_view(), name="upcoming"),
]
