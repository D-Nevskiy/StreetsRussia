from rest_framework import serializers

from events.models import (
    Event,
    GalleryEvent,
    Location,
    Discipline,
    SubDiscipline,
    TypeEvent,
    City,
    Region
)


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
            'id',
            'name',
        )


class SubDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDiscipline
        fields = (
            'id',
            'name',
            'discipline',
        )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = (
            'id',
            'name',
            'region',
        )


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'owner',
            'code',
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
