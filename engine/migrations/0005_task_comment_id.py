# Generated by Django 5.0.2 on 2024-03-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0004_task_base_task_head_task_pr_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comment_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
