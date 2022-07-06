from enum import unique
import uuid
from django.db import models

# Create your models here.
class Booking(models.Model):
    SITE = (
        ('Papatoetoe', 'Papatoetoe'),
        ('Onehunga','Onehunga')
    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField()
    location = models.CharField(max_length=200, choices=SITE)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_chosen = models.DateField(null=True)
    time_chosen = models.TimeField(null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['name','phone']]