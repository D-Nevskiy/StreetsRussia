from partners.models import Partner
from rest_framework import serializers


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'name', 'image', 'description')
