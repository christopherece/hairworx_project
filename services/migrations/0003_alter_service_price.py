# Generated by Django 4.0.5 on 2022-07-01 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_services_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
