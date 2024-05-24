from feedback.models import Feedback
from rest_framework import serializers


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'ip_address',
            'content',
            'email',
            'phone_number',
            'consent_to_rights',
            'сonsent_to_processing'
        )
        read_only_fields = (
            'user',
            'ip_address'
        )
