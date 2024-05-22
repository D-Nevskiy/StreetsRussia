from django.contrib import admin
from user.models import UserAccount


@admin.register(UserAccount)
class UserAccount(admin.ModelAdmin):
    """
    Конфигурация модели UserAccount для административной панели.
    """
    pass
