# Generated by Django 4.0.5 on 2022-07-03 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
