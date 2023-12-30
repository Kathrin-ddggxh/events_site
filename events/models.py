from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class UpcomingEvent(models.Model):
    """
    Model to create and manage upcoming events
    """

    user = models.ForeignKey(
        User,
        related_name="event_uploader",
        on_delete=models.SET_DEFAULT,
        default="not found",
    )
    location = models.CharField(max_length=300, null=False, blank=False)
    venue = models.CharField(max_length=300, null=False, blank=False)
    datetime = models.DateTimeField(null=False, blank=False)
    admission = models.DecimalField(
        max_digits=5, decimal_places=2, null=False, blank=False
    )
    max_tickets = models.IntegerField(validators=[MaxValueValidator(10000)])
    cancelled = models.BooleanField(default=False)
