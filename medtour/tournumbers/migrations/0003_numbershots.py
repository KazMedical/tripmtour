# Generated by Django 3.2.15 on 2023-02-14 10:36

from django.db import migrations, models
import django.db.models.deletion
import medtour.tournumbers.instances
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tournumbers', '0002_auto_20230213_2305'),
    ]

    operations = [
        migrations.CreateModel(
            name='NumberShots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('photo', sorl.thumbnail.fields.ImageField(upload_to=medtour.tournumbers.instances.get_shots_path, verbose_name='Изображение')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя изображения')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournumbers.tournumbers', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Изображение номера',
                'verbose_name_plural': 'Изображения номера',
            },
        ),
    ]
