from events.models import (City, Discipline, Event, GalleryEvent, Location,
                           Region, SubDiscipline, TypeEvent)
from api.v1.serializers.user import UserSmallSerializer
from rest_framework import serializers
from django.shortcuts import get_object_or_404


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
    author = UserSmallSerializer(read_only=True)

    def create(self, validated_data):
        discipline_data = validated_data.pop('discipline')
        sub_discipline_data = validated_data.pop('sub_discipline')
        type_of_event_data = validated_data.pop('type_of_event')
        location_data = validated_data.pop('location')

        discipline = get_object_or_404(
            Discipline,
            **discipline_data
        )
        sub_discipline = get_object_or_404(
            SubDiscipline,
            discipline=discipline,
            **sub_discipline_data
        )
        type_of_event = get_object_or_404(
            TypeEvent,
            **type_of_event_data
        )

        location, created = Location.objects.get_or_create(
            **location_data
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
            'author',
        )


class EventSmallReadSerializer(EventSerializer):
    class Meta:
        model = Event
        fields = (
            'title',
            'start_datetime',
            'location',
            'files',
            'author',
            'organizers_contact',
        )
