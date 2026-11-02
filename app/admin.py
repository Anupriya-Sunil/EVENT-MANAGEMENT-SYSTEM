
from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'event_date',
        'event_time',
        'category',
        'location',
        'is_completed'
    )

    list_filter = ('category', 'is_completed', 'event_date')

    search_fields = ('event_name', 'location')

