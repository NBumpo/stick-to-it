# Generated by Django 5.0 on 2023-12-19 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_todo_todo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='complete',
        ),
    ]
