from rest_framework import generics, permissions, status, views
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from api.v1.permissions import IsAdminOrCreateOnly
from api.v1.serializers.user import (ChangePasswordSerializer,
                                     UserAccountSerializer,
                                     UserApprovalSerializer)
from user.models import UserAccount


class SignupView(generics.CreateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer
    permission_classes = (IsAdminOrCreateOnly,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Когда ваши данные будут проверены.'
                            'Вы получите электронное письмо с вашим паролем.'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(ObtainAuthToken):
    permission_classes = (IsAdminOrCreateOnly,)

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
        if not user.is_active:
            UserAccount.objects.approve_user(user)
            return Response(
                {'message': 'Данные пользователя верны. '
                            'Пользователь одобрен. Временный пароль отправлен '
                            'на электронную почту.'},
                status=status.HTTP_200_OK
            )
        return Response(
            {'message': 'Пользователь уже подтверждён.'},
            status=status.HTTP_400_BAD_REQUEST
        )
