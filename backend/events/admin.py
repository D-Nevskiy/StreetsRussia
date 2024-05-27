from django.contrib import admin, messages

from .models import (City, Discipline, Event, GalleryEvent, Location, Region,
                     SubDiscipline, TypeEvent, EventRegistration)


class GalleryEventInline(admin.TabularInline):
    """
    Inline-класс для отображения галереи мероприятия в админ панели.
    Этот класс позволяет отображать галерею мероприятия
    в виде таблицы в админ панели.
    """
    model = GalleryEvent


@admin.action(description='Подтвердить выбранное мероприятие')
def confirm_event(modeladmin, request, queryset):
    queryset.update(is_moderation=True)
    modeladmin.message_user(
        request,
        f'Мероприятие(я) {queryset} подтверждено(ы)',
        messages.SUCCESS
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Event.
    """
    inlines = (GalleryEventInline,)
    actions = [confirm_event,]


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


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Registration
    """
    pass
