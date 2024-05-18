from rest_framework import viewsets, views, permissions
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django_filters.rest_framework import DjangoFilterBackend

from events.models import Event
from news.models import News, Category
from user.models import UserAccount
from api.v1.serializers import (
    CategorySerializer,
    NewsSerializer,
    EventSerializer,
    EventSmallReadSerializer,
    UserAccountSerializer,
    ChangePasswordSerializer,
    UserApprovalSerializer
)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('discipline_of_event', 'date', 'city')

    def get_queryset(self):
        return Event.objects.filter(is_moderation=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EventSmallReadSerializer
        elif self.action == 'retrieve':
            return EventSerializer
        return EventSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('category', )


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SignupView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {'message':  'Когда ваши данные будут проверены. \
                    Вы получите электронное письмо с вашим паролем.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            token, create = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = UserAccount

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.objects = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.objects.check_password(
                serializer.data.get('old_password')
            ):
                return Response(
                    {'old_password': 'Wrong password.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            self.objects.set_password(serializer.data.get('new_password'))
            self.objects.save()
            return Response(
                {'status': 'success',
                 'message': 'Password updated successfully.'},
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserApprovalView(generics.UpdateAPIView):
    queryset = UserAccount.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserApprovalSerializer

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        if user.status == UserAccount.Status.UNCONFIRMED:
            UserAccount.objects.approve_user(user)
            return Response(
                {'message': 'Данные пользователя верны. Пользователь одобрен. \
                    Временный пароль отправлен на электронную почту.'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'Пользователь уже подтверждён.'},
            status=status.HTTP_400_BAD_REQUEST
        )
