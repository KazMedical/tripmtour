# Generated by Django 3.2.15 on 2023-03-23 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0002_guideprogram_program_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guideservices',
            name='org',
        ),
        migrations.AddField(
            model_name='guideservices',
            name='guide',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='guide_services', to='guides.guide', verbose_name='Гид'),
            preserve_default=False,
        ),
    ]
