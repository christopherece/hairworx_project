# Generated by Django 4.0.6 on 2022-07-14 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_worksite'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookings.site'),
        ),
    ]
