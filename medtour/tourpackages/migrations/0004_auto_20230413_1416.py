# Generated by Django 3.2.15 on 2023-04-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourpackages', '0003_alter_tourpackages_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpackages',
            name='remarks',
            field=models.CharField(blank=True, default='Примечание', max_length=1000, null=True, verbose_name='Примечание'),
        ),
        migrations.AlterField(
            model_name='tourpackages',
            name='title',
            field=models.CharField(help_text='Примерное наименование: Комфорт, Стандарт, Номер на 1 человек', max_length=1000, verbose_name='Название пакета'),
        ),
        migrations.AlterField(
            model_name='tourpackagesservices',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Услуга сервиса'),
        ),
    ]
