
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Event
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all().order_by('event_date')
    serializer_class = EventSerializer

    # Pending Events
    @action(detail=False, methods=['get'])
    def pending(self, request):
        events = Event.objects.filter(is_completed=False)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    # Completed Events
    @action(detail=False, methods=['get'])
    def completed(self, request):
        events = Event.objects.filter(is_completed=True)
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)

    # Upcoming Events
    @action(detail=False, methods=['get'])
    def upcoming(self, request):
        events = Event.objects.filter(
            event_date__gte=timezone.localdate(),
            is_completed=False
        )
        serializer = self.get_serializer(events, many=True)
        return Response(serializer.data)
   
    @action(detail=True, methods=['patch'])
    def mark_completed(self, request, pk=None):
        event = self.get_object()
        event.is_completed = True
        event.save()

        serializer = self.get_serializer(event)
        return Response({
            'message': 'Event marked as completed',
            'event': serializer.data
        })

    