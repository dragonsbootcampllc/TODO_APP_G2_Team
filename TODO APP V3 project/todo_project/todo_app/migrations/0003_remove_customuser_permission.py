# Generated by Django 4.2.4 on 2023-09-02 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_customuser_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='permission',
        ),
    ]
