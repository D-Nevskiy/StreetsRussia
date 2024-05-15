from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import NewsViewSet, CategoryViewSet


router = DefaultRouter()
router.register('news', NewsViewSet, basename='news')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
