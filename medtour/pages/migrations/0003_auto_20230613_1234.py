# Generated by Django 3.2.15 on 2023-06-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20230406_1034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.DeleteModel(
            name='AboutTheProject',
        ),
        migrations.DeleteModel(
            name='Contacts',
        ),
        migrations.DeleteModel(
            name='Stocks',
        ),
    ]
