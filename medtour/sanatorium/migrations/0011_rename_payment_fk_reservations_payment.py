# Generated by Django 3.2.15 on 2023-05-31 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sanatorium', '0010_alter_reservations_approved_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='payment_fk',
            new_name='payment',
        ),
    ]
