from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from news.models import Category, News
from api.v1.serializers.news import CategorySerializer, NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
