# Generated by Django 3.2.15 on 2023-03-28 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0004_guide_working_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='category',
        ),
    ]
