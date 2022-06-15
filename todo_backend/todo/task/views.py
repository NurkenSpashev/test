from .serializers import TaskSerializer
from .models import Task

from django.core.mail import send_mail

from rest_framework import viewsets
import json


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(author=user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        if request.method == 'PATCH':
            data = json.loads(request.body)
            task = Task.objects.get(pk=data.get('id'))
            email = request.user.email
            subject = "Sending an email with Django"
            message = f"Dear, {email}, task {task.title} was updated."

            send_mail(subject, message, 's.nurken92@gmail.com', [email])
        return super().update(request, *args, **kwargs)

