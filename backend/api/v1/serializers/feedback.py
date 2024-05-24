from rest_framework import serializers

from feedback.models import Feedback


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
            'content',
            'email',
            'phone_number',
            'consent_to_rights',
            'сonsent_to_processing'
        )
        read_only_fields = (
            'user',
        )
