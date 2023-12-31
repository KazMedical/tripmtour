# Generated by Django 3.2.15 on 2023-02-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20230212_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourMedicalProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Медицинский профиль',
                'verbose_name_plural': 'Медицинские профили',
            },
        ),
        migrations.AddField(
            model_name='tour',
            name='medical_profiles',
            field=models.ManyToManyField(blank=True, related_name='tours', to='tours.TourMedicalProfile'),
        ),
    ]
