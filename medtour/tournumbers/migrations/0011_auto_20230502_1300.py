# Generated by Django 3.2.15 on 2023-05-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournumbers', '0010_auto_20230413_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournumbers',
            name='extra_capacity_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Цена за доп. место'),
        ),
        migrations.AddField(
            model_name='tournumbers',
            name='max_capacity',
            field=models.IntegerField(blank=True, default=1, verbose_name='Макс. Вместимость'),
        ),
    ]
