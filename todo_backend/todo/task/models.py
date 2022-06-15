from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Task(models.Model):
    STATUS = (
        (True, 'Done'),
        (False, 'Undone')
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name='Task Title', db_index=True)
    description = models.TextField(verbose_name='Task Description')
    status = models.BooleanField(verbose_name='Task Status', default=False, choices=STATUS)
    created_at = models.DateTimeField(verbose_name='Task Created', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['created_at']
