from rest_framework import serializers

from news.models import News, NewsImage, Category


class NewsImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsImage
        fields = ('id', 'image', )


class NewsSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True, source='news_images')

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'category',
            'description',
            'link',
            'age_restriction',
            'images',
        )

    def create(self, validated_data):
        images_data = self.context.get('request').FILES.getlist('images')
        categories_data = validated_data.pop('category', [])
        news = News.objects.create(**validated_data)
        for category_data in categories_data:
            category_instance = Category.objects.get(name=category_data)
            news.category.add(category_instance)
        for image_data in images_data:
            NewsImage.objects.create(news=news, image=image_data)
        return news


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', )
