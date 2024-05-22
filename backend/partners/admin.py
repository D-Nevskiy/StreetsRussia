from django.contrib import admin

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Partner.
    """
    pass
