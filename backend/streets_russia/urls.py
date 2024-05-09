from django.contrib import admin
from django.urls import path
from .yasg_setting import urlpatterns as yasg_setting_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += yasg_setting_urls
