# Generated by Django 3.2.15 on 2023-03-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_tour_deleted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='working_time',
            field=models.TextField(blank=True, null=True, verbose_name='Время работы'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='is_deleted',
            field=models.BooleanField(db_index=True, default=False, editable=False, help_text='Отметьте, если удалён тур', verbose_name='Удалён?'),
        ),
    ]