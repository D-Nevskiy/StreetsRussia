from api.v1.permissions import IsAdminOrReadOnly
from api.v1.serializers.partners import PartnerSerializer
from django_filters.rest_framework import DjangoFilterBackend
from partners.models import Partner
from rest_framework import viewsets


class PartherViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
