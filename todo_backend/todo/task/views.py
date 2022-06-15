from .serializers import TaskSerializer
from .models import Task
from .tasks import send_message

from rest_framework import viewsets
from django.core import serializers
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
            task = Task.objects.filter(pk=data.get('id'))
            data = serializers.serialize('json', task)
            email = request.user.email

            send_message.delay(email, data)

        return super().update(request, *args, **kwargs)

