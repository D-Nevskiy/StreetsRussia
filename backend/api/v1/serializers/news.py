from news.models import Category, GalleryNews, News
from rest_framework import serializers


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
