from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.v1.views import (
    NewsViewSet,
    CategoryViewSet,
    EventViewSet,
    UserApprovalView,
    SignupView,
    LoginView,
    LogoutView,
    ChangePasswordView,
    UserProfileView
)

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('news', NewsViewSet, basename='news')
router.register('category', CategoryViewSet, basename='category')


urlpatterns = [
    path('', include(router.urls)),
    path('user/approve/<uuid:pk>/', UserApprovalView.as_view(), name='useraccount-approve'),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('auth/profile/', UserProfileView.as_view(), name='user_profile')
]
