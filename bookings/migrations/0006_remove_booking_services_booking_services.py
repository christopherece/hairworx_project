# Generated by Django 4.0.6 on 2022-07-10 03:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_booking_stylist_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='services',
        ),
        migrations.AddField(
            model_name='booking',
            name='services',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None),
        ),
    ]
