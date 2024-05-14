from django.contrib import admin
from news.models import News, NewsImage, Category


class NewsImageInline(admin.TabularInline):
    """
    Inline-модель для административной панели Django,
    предназначенная для отображения и редактирования изображений
    связанных с моделью News.
    """
    model = NewsImage
    extra = 5


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Конфигурация модели Advertisement для административной панели.
    """
    list_display = ['id',
                    'title',
                    'link',
                    'start_date',
                    'end_date',
                    'age_restriction',
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


@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    """
    Конфигурация модели NewsImage для административной панели.
    """
    list_display = ['news', 'image']
    list_filter = ('news', )
