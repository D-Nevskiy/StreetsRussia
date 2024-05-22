from rest_framework import serializers

from events.models import (Discipline, Event, GalleryEvent, Location,
                           SubDiscipline, TypeEvent)


class TypeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEvent
        fields = (
            'name',
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'name',
            'region',
            'city',
            'type_of_area',
            'address',
        )


class DisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discipline
        fields = (
            'name',
        )


class SubDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDiscipline
        fields = (
            'name',
        )


class GalleryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryEvent
        fields = ('file',)


class EventSerializer(serializers.ModelSerializer):
    files = GalleryEventSerializer(
        many=True,
        read_only=True,
        source='gallery_events'
    )
    discipline = DisciplineSerializer()
    sub_discipline = SubDisciplineSerializer()
    type_of_event = TypeEventSerializer()
    location = LocationSerializer()

    def create(self, validated_data):
        files_data = self.context.get('request').FILES.getlist('images')
        event = Event.objects.create(**validated_data)
        for file in files_data:
            GalleryEvent.objects.create(event=event, file=file)

    class Meta:
        model = Event
        fields = (
            'files',
            'title',
            'description',
            'start_datetime',
            'end_datetime',
            'discipline',
            'sub_discipline',
            'type_of_event',
            'location',
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
            'discipline',
            'start_datetime',
            'end_datetime',
            'location',
            'files',
        )
