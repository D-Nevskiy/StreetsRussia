from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.v1.serializers import (CategorySerializer, EventSerializer,
                                EventSmallReadSerializer, NewsSerializer)
from events.models import Event
from news.models import Category, News


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('discipline_of_event', 'date', 'city')

    def get_queryset(self):
        return Event.objects.filter(is_moderation=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSmallReadSerializer
        if self.action == 'retrieve':
            return EventSerializer
        return EventSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('category', )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
