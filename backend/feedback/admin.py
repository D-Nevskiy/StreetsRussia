from django.contrib import admin

from feedback.models import Feedback, FeedbackProcessing


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Класс администратора для модели Feedback.
    """
    pass


@admin.register(FeedbackProcessing)
class FeedbackProcessing(admin.ModelAdmin):
    """
    Класс администратора для модели FeedbackProcessing.
    """
    pass
