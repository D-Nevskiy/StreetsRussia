from rest_framework import serializers

from feedback.models import Feedback, FeedbackProcessing


class FeedbackSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        consent_to_rights = validated_data.pop('consent_to_rights')
        consent_to_processing = validated_data.pop('сonsent_to_processing')
        if not consent_to_rights:
            raise serializers.ValidationError(
                'Необходимо согласие на правила сообщества'
            )
        if not consent_to_processing:
            raise serializers.ValidationError(
                'Необходимо согласие на обработку персональных данных'
            )
        feedback = Feedback.objects.create(**validated_data)
        return feedback

    class Meta:
        model = Feedback
        fields = (
            'id',
            'user',
            'name',
            'content',
            'email',
            'phone_number',
            'consent_to_rights',
            'consent_to_processing',
            'status',
        )
        read_only_fields = (
            'user',
            'status',
        )


class FeedbackProcessingSerializer(serializers.ModelSerializer):
    feedback = FeedbackSerializer(
        many=True,
        source='feedback_processing',
        read_only=True
    )

    class Meta:
        model = FeedbackProcessing
        fields = (
            'id',
            'feedback',
            'text',
            'support_agent',
        )
        read_only_fields = (
            'support_agent',
        )
