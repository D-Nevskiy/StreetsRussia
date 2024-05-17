from rest_framework import serializers

from events.models import Event, GalleryEvent
from news.models import Category, GalleryNews, News


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


class GalleryNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GalleryNews
        fields = ('id', 'file', )


class NewsSerializer(serializers.ModelSerializer):
    files = GalleryNewsSerializer(
        many=True,
        read_only=True,
        source='news_images'
    )

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'category',
            'description',
            'files',
        )

    def create(self, validated_data):
        files_data = self.context.get('request').FILES.getlist('images')
        categories_data = validated_data.pop('category', [])
        news = News.objects.create(**validated_data)
        for category_data in categories_data:
            category_instance = Category.objects.get(name=category_data)
            news.category.add(category_instance)
        for file_data in files_data:
            GalleryNews.objects.create(news=news, file=file_data)
        return news


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', )
