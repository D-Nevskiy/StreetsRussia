from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.v1.serializers.events import EventSerializer, EventSmallReadSerializer
from events.models import Event


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('discipline', 'start_datetime')

    def get_queryset(self):
        return Event.objects.filter(is_moderation=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSmallReadSerializer
        if self.action == 'retrieve':
            return EventSerializer
        return EventSerializer
