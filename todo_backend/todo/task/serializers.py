from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'author']
