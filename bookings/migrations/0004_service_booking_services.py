# Generated by Django 4.0.6 on 2022-07-09 12:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_booking_time_chosen_alter_booking_date_chosen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='services',
            field=models.ManyToManyField(blank=True, to='bookings.service'),
        ),
    ]