# Generated by Django 4.1.9 on 2023-08-02 10:11

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("guides", "0030_alter_programschedule_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="programplaces",
            name="description",
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name="Описание местности"),
        ),
    ]
