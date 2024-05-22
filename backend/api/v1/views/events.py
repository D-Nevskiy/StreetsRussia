from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins

from events.models import (
    Event,
    Discipline,
    SubDiscipline,
    TypeEvent,
    Region,
    City
)
from api.v1.serializers.events import (
    EventSerializer,
    EventSmallReadSerializer,
    SubDisciplineSerializer,
    DisciplineSerializer,
    TypeEventSerializer,
    CitySerializer,
    RegionSerializer
)


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


class DisciplineViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    filter_backends = (DjangoFilterBackend,)


class SubDisciplineViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = SubDiscipline.objects.all()
    serializer_class = SubDisciplineSerializer
    filter_backends = (DjangoFilterBackend,)


class TypeEventViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = TypeEvent.objects.all()
    serializer_class = TypeEventSerializer
    filter_backends = (DjangoFilterBackend,)


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)


class RegionViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    filter_backends = (DjangoFilterBackend,)
