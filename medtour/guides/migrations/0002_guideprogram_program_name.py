# Generated by Django 3.2.15 on 2023-03-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideprogram',
            name='program_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Название программы'),
            preserve_default=False,
        ),
    ]