# Generated by Django 4.1.9 on 2023-06-26 14:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("guides", "0024_guideprogram_category_guideprogram_city_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="guideprogram",
            old_name="name",
            new_name="title",
        ),
    ]
