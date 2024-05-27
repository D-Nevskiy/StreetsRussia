from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from api.v1.serializers.feedback import (FeedbackProcessingSerializer,
                                         FeedbackSerializer)
from feedback.models import Feedback, FeedbackProcessing
from feedback.tasks import send_email_task_feedback


class FeedbackView(generics.CreateAPIView,
                   generics.ListAPIView,
                   generics.RetrieveAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('status',)
    throttle_scope = 'feedback_request'

    def get_permissions(self):
        if self.request.method == 'GET':
            return (permissions.IsAdminUser(),)
        return (permissions.AllowAny(),)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_create(self, serializer):
        user = (self.request.user
                if self.request.user.is_authenticated else None)
        serializer.save(user=user)


class FeedbackProcessingView(generics.CreateAPIView,
                             generics.ListAPIView,
                             generics.RetrieveAPIView):
    queryset = FeedbackProcessing.objects.all()
    serializer_class = FeedbackProcessingSerializer
    permission_classes = (permissions.IsAdminUser,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        instance = response.data
        self.send_feedback_response_email(instance)
        return response

    def send_feedback_response_email(self, instance):
        feedback = get_object_or_404(Feedback, pk=instance.get('feedback'))
        email = feedback.email
        subject = (f'Ответ на вашу заявку от '
                   f'{feedback.created_at.strftime("%d.%m.%Y")}')
        context = {'subject': subject, 'text': instance.get('text'),
                   'obj': feedback}
        html_message = render_to_string('response_feedback.html',
                                        context)
        plain_message = strip_tags(html_message)
        send_email_task_feedback.delay(
            subject,
            plain_message,
            [email],
            html_message
        )

    def perform_create(self, serializer):
        serializer.save(support_agent=self.request.user)
