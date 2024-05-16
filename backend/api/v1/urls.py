from rest_framework.routers import SimpleRouter
from django.urls import include, path

from api.v1.views import NewsViewSet, CategoryViewSet, EventViewSet

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('news', NewsViewSet, basename='news')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
