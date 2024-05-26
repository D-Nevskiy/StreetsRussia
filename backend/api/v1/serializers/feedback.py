from rest_framework import serializers

from feedback.models import Feedback, FeedbackProcessing


class FeedbackSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        consent_to_rights = validated_data.get('consent_to_rights')
        consent_to_processing = validated_data.get('consent_to_processing')
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
    is_closed = serializers.BooleanField(write_only=True)

    def create(self, validated_data):
        is_closed = validated_data.pop('is_closed')
        feedback = validated_data.get('feedback')
        feedback.status = 'CLOSED' if is_closed else 'PENDING'
        feedback.save()
        return FeedbackProcessing.objects.create(**validated_data)

    class Meta:
        model = FeedbackProcessing
        fields = (
            'id',
            'feedback',
            'text',
            'support_agent',
            'is_closed',
        )
        read_only_fields = (
            'support_agent',
        )
