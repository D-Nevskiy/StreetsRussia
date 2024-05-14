from rest_framework import serializers
from events.models import Event
from django.utils import timezone


class EventSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    @staticmethod
    def validate_date(value):
        if value <= timezone.now().date():
            raise serializers.ValidationError(
                "Дата мероприятия не может быть прошедшей"
            )
        return value

    class Meta:
        model = Event
        exclude = ('is_moderation', 'count_entrant')


class EventSmallReadSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'picture',
            'title',
            'discipline_of_event',
            'date',
            'city',
        )
