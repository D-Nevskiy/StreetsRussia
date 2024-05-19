from django.contrib import admin
from django.urls import include, path

from .yasg_setting import urlpatterns as yasg_setting_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
]

urlpatterns += yasg_setting_urls

# urlpatterns += [
#     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
#     path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
#
# ]
