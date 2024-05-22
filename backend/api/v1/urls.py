from api.v1.views.events import (CityViewSet, DisciplineViewSet, EventViewSet,
                                 RegionViewSet, SubDisciplineViewSet,
                                 TypeEventViewSet)
from api.v1.views.news import CategoryViewSet, NewsViewSet
from api.v1.views.partners import PartherViewSet
from api.v1.views.user import (ChangePasswordView, LoginView, LogoutView,
                               SignupView, UserApprovalView, UserProfileView)
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('events', EventViewSet, basename='events')
router.register('news', NewsViewSet, basename='news')
router.register('discipline', DisciplineViewSet, basename='discipline')
router.register(
    'sub-discipline',
    SubDisciplineViewSet,
    basename='sub discipline'
)
router.register('type-event', TypeEventViewSet, basename='type-event')
router.register('category', CategoryViewSet, basename='category')
router.register('partners', PartherViewSet, basename='parthers')
router.register('city', CityViewSet, basename='city')
router.register('region', RegionViewSet, basename='region')


urlpatterns = [
    path('', include(router.urls)),
    path(
        'user/approve/<uuid:pk>/',
        UserApprovalView.as_view(),
        name='useraccount-approve'
    ),
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path(
        'auth/change-password/',
        ChangePasswordView.as_view(),
        name='change-password'
    ),
    path('auth/profile/', UserProfileView.as_view(), name='user_profile')
]
