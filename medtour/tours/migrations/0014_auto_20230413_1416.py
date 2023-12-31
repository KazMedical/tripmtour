# Generated by Django 3.2.15 on 2023-04-13 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0013_alter_tourbookingweekdays_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfoservices',
            name='service',
            field=models.CharField(max_length=1000, verbose_name='Наименование услуги'),
        ),
        migrations.AlterField(
            model_name='additionaltitles',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tour',
            name='address',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='tour',
            name='district',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Район'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя директора'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия директора'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='requisites',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Для предоплаты (IBAN)'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='street',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название тура'),
        ),
        migrations.AlterField(
            model_name='tour',
            name='youtube_url',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ссылка на Youtube'),
        ),
        migrations.AlterField(
            model_name='tourpaidservices',
            name='name',
            field=models.CharField(help_text='Наименование платной услуги', max_length=1000, verbose_name='Название услуги'),
        ),
        migrations.AlterField(
            model_name='tourphones',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='tourshots',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Имя изображения'),
        ),
    ]
