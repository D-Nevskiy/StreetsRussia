from api.v1.permissions import IsAdminOrReadOnly
from api.v1.serializers.news import CategorySerializer, NewsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from news.models import Category, News
from rest_framework import viewsets


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
