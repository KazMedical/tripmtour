# Generated by Django 4.1.9 on 2023-06-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_auto_20230608_1858"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="organizationcategory",
            name="icon_active",
        ),
        migrations.AddField(
            model_name="organizationcategory",
            name="is_main",
            field=models.BooleanField(default=False),
        ),
    ]
