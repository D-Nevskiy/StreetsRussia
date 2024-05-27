from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from api.v1.permissions import IsAdminOrCreateOnly, IsAdminOrReadOnly
from api.v1.serializers.events import (CitySerializer, DisciplineSerializer,
                                       EventRegistrationSerializer,
                                       EventSerializer,
                                       EventSmallReadSerializer,
                                       RegionSerializer,
                                       SubDisciplineSerializer,
                                       TypeEventSerializer)
from events.models import (City, Discipline, Event, EventRegistration, Region,
                           SubDiscipline, TypeEvent)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = (
        'discipline',
        'start_datetime',
        'location__city',
        'location__region',
        'discipline',
        'sub_discipline',
    )

    def get_queryset(self):
        return Event.objects.filter(is_moderation=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSmallReadSerializer
        if self.action == 'retrieve':
            return EventSerializer
        return EventSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DisciplineViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Discipline.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = DisciplineSerializer
    filter_backends = (DjangoFilterBackend,)


class SubDisciplineViewSet(mixins.ListModelMixin,
                           mixins.RetrieveModelMixin,
                           viewsets.GenericViewSet):
    queryset = SubDiscipline.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = SubDisciplineSerializer
    filter_backends = (DjangoFilterBackend,)


class TypeEventViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    queryset = TypeEvent.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = TypeEventSerializer
    filter_backends = (DjangoFilterBackend,)


class CityViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = City.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = CitySerializer
    filter_backends = (DjangoFilterBackend,)


class RegionViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Region.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = RegionSerializer
    filter_backends = (DjangoFilterBackend,)


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = (IsAdminOrCreateOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('user', 'event')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
