# Generated by Django 3.2.15 on 2023-06-13 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0018_programplaces_programschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guideprogram',
            name='description',
        ),
        migrations.RemoveField(
            model_name='guideprogram',
            name='program',
        ),
    ]
