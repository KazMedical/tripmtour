# Generated by Django 3.2.15 on 2023-03-26 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0011_alter_commenttour_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='working_hours',
        ),
    ]
