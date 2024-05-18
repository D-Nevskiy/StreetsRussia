from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from events.models import Event, GalleryEvent
from news.models import News, GalleryNews, Category
from user.models import UserAccount


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
        fields = ('id', 'file',)


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
        fields = ('id', 'name',)


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = [
            'email',
            'first_name',
            'last_name',
            'middle_name',
            'date_of_birth',
            'phone_number',
            'city',
            'passport_series',
            'passport_number',
            'passport_issue_date',
            'passport_issued_by',
            'consent_to_rights',
            'сonsent_to_processing'
        ]

    def create(self, validated_data):
        return UserAccount.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(
        required=True,
        validators=[validate_password]
    )
    new_password_confirm = serializers.CharField(required=True)

    def validate(self, attrs):
        new_password = attrs.get('new_password')
        new_password_confirm = attrs.get('new_password_confirm')

        if new_password != new_password_confirm:
            raise serializers.ValidationError(
                {'message': 'Пароли не совпадают.'}
            )

        return attrs


class UserApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'status']
