from django.contrib import admin

from .models import (City, Discipline, Event, GalleryEvent, Location, Region,
                     SubDiscipline, TypeEvent)


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


@admin.register(SubDiscipline)
class SubDisciplineAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели SubDiscipline.
    """
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Region.
    """
    pass


@admin.register(TypeEvent)
class TypeEventAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели TypeEvent.
    """
    pass


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Location.
    """
    pass
