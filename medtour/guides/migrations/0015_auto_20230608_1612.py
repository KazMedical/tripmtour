# Generated by Django 3.2.15 on 2023-06-08 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guides', '0014_auto_20230607_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='guidecategory',
            name='icons',
            field=models.ImageField(default='/static/images/cart.svg', upload_to='category_icons'),
        ),
        migrations.AddField(
            model_name='guidecategory',
            name='photo',
            field=models.ImageField(default='/static/images/default.svg', upload_to='banners'),
        ),
    ]
