from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

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
        discipline_data = validated_data.pop('discipline')
        sub_discipline_data = validated_data.pop('sub_discipline')
        type_of_event_data = validated_data.pop('type_of_event')
        location_data = validated_data.pop('location')

        try:
            discipline = Discipline.objects.get(**discipline_data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Такой дисциплины не существует"
            )

        try:
            sub_discipline = SubDiscipline.objects.get(
                discipline=discipline,
                **sub_discipline_data
            )
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Такой поддисциплины не существует"
            )

        try:
            type_of_event = TypeEvent.objects.get(**type_of_event_data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Такого типа мероприятия не существует"
            )

        try:
            location = Location.objects.get(**location_data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Такой локации не существует"
            )

        event = Event.objects.create(
            discipline=discipline,
            sub_discipline=sub_discipline,
            type_of_event=type_of_event,
            location=location,
            **validated_data
        )

        files_data = self.context.get('request').FILES.getlist('images')
        for file in files_data:
            GalleryEvent.objects.create(event=event, file=file)

        return event

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
            'author'
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
