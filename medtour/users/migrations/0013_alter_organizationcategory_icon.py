# Generated by Django 4.1.9 on 2023-06-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_remove_organizationcategory_icon_active_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationcategory",
            name="icon",
            field=models.FileField(default="/static/images/cart.svg", upload_to="category_icons"),
        ),
    ]