from rest_framework import serializers
from events.models import Event, GalleryEvent


class GalleryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryEvent
        fields = ('file',)


class EventSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    files = GalleryEventSerializer(
        many=True,
        read_only=True,
        source='gallery_events'
    )

    def create(self, validated_data):
        files_data = self.context.get('request').FILES.getlist('images')
        event = Event.objects.create(**validated_data)
        for file in files_data:
            GalleryEvent.objects.create(event=event, file=file)
        return event

    class Meta:
        model = Event
        fields = (
            'title',
            'files',
            'description',
            'date',
            'discipline_of_event',
            'type_of_area',
            'plan_of_event',
            'city',
            'address',
            'organizers_contact',
        )


class EventSmallReadSerializer(EventSerializer):
    files = GalleryEventSerializer(
        many=True,
        read_only=True,
        source='gallery_events'
    )

    class Meta:
        model = Event
        fields = (
            'title',
            'discipline_of_event',
            'date',
            'city',
            'files',
        )
