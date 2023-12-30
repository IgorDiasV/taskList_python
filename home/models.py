from django.db import models


class TaskDay(models.Model):
    id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    done_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.id} {self.day}'


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)
    task_day = models.ManyToManyField(TaskDay)

    def __str__(self):
        return self.task_name