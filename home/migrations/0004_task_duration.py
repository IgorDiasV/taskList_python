# Generated by Django 4.2.4 on 2024-01-09 23:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_taskday_done_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="duration",
            field=models.IntegerField(default=0),
        ),
    ]
