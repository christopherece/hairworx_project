from enum import unique
from unicodedata import name
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Booking(models.Model):
    SITE = (
        ('Papatoetoe', 'Papatoetoe'),
        ('Onehunga','Onehunga')
    )
    STYLIST = (
        ('No Prefered','No Prefered'),
        ('Arnie','Arnie'),
        ('Dana','Dana'),
        ('Purvi Alison', 'Purvi Alison'),
        ('Ailyn', 'Ailyn'),
        ('Mary','Mary'),
        ('Alison','Alison')

    )
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField()
    stylist_name = models.CharField(max_length=200, choices=STYLIST, null=True,blank=True)
    location = models.CharField(max_length=200, choices=SITE)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_chosen = models.DateField(null=True)
    time_chosen = models.TimeField(null=True)
    services = ArrayField(models.CharField(max_length=200), blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['name','phone']]

    def __str__(self):
        return '{}'.format(self.name)

class Service(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name