# Generated by Django 4.1.9 on 2023-06-27 03:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0004_remove_application_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="type",
            field=models.CharField(
                choices=[("tours", "Tours"), ("guide-programs", "Guide programs")], max_length=20, verbose_name="Тип"
            ),
        ),
    ]
