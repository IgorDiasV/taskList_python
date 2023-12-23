from django.contrib import admin
from .models import Task, TaskDay

admin.site.register(Task)
admin.site.register(TaskDay)