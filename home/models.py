from django.db import models


class TaskDay(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=50)
    done = models.BooleanField(default=False)


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    task_day = models.ManyToManyField(TaskDay)