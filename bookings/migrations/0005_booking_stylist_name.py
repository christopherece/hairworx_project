# Generated by Django 4.0.6 on 2022-07-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_service_booking_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='stylist_name',
            field=models.CharField(blank=True, choices=[('Arnie', 'Arnie'), ('Dana', 'Dana')], max_length=200, null=True),
        ),
    ]