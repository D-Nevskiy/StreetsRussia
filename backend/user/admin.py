from django.contrib import admin, messages
from user.models import UserAccount


@admin.action(description='Подтвердить выбранного пользователя')
def confirm_user(modeladmin, request, queryset):
    for user in queryset:
        UserAccount.objects.approve_user(user)
        modeladmin.message_user(
            request,
            f'Пользователь(и) {user} подтверждён(ы)',
            messages.SUCCESS
        )


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    """
    Конфигурация модели UserAccount для административной панели.
    """
    actions = [confirm_user]
