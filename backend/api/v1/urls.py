from rest_framework.routers import SimpleRouter
from django.urls import include, path

from .views import EventViewSet

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]