
from django.db import models


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name
