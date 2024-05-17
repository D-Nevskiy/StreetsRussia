from django.contrib import admin

from news.models import Category, GalleryNews, News


class NewsImageInline(admin.TabularInline):
    """
    Inline-модель для административной панели Django,
    предназначенная для отображения и редактирования изображений
    связанных с моделью News.
    """
    model = GalleryNews
    extra = 5


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Конфигурация модели News для административной панели.
    """
    list_display = [
        'id',
        'title',
        'created_at',
    ]

    list_filter = ('title', 'category')
    inlines = [NewsImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Category для административной панели.
    """
    list_display = ['name']
    list_filter = ('name', )


@admin.register(GalleryNews)
class GalleryNewsAdmin(admin.ModelAdmin):
    """
    Конфигурация модели GalleryNews для административной панели.
    """
    list_display = ['news', 'file']
    list_filter = ('news', )
