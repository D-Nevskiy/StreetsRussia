from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1.views import CategoryViewSet, EventViewSet, NewsViewSet

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('news', NewsViewSet, basename='news')
router.register('category', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]
