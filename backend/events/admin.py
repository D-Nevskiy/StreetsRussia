from django.contrib import admin

from .models import City, Discipline, Event, GalleryEvent


class GalleryEventInline(admin.TabularInline):
    """
    Inline-класс для отображения галереи мероприятия в админ панели.
    Этот класс позволяет отображать галерею мероприятия
    в виде таблицы в админ панели.
    """
    model = GalleryEvent


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Event.
    """
    inlines = (GalleryEventInline,)


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Discipline.
    """
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели City.
    """
    pass
