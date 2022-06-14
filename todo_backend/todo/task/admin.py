from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "description", "status", "created_at")
    ist_filter = ("status",)
    search_fields = ("title", )
    list_editable = ('status',)
