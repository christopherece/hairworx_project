# Generated by Django 4.0.6 on 2022-07-11 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_booking_stylist_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
