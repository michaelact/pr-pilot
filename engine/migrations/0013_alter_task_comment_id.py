# Generated by Django 5.0.3 on 2024-04-12 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("engine", "0012_task_task_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="comment_id",
            field=models.IntegerField(null=True),
        ),
    ]
