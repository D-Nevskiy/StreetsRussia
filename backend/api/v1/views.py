from rest_framework import viewsets
from events.models import Event
from .serializers import EventSerializer, EventSmallReadSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('discipline_of_event', 'date', 'city')

    def get_queryset(self):
        return Event.objects.filter(is_moderation=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSmallReadSerializer
        elif self.action == 'retrieve':
            return EventSerializer
        return EventSerializer
