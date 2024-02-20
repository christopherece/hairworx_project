from statistics import mode
from unicodedata import name
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name




class Site(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    SITE = (
        ('1', 'Onehunga'),
        ('2','Papatoetoe')
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
    site = models.ForeignKey('Site',  on_delete=models.DO_NOTHING, null=True, blank=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.IntegerField()
    stylist_name = models.CharField(max_length=200, choices=STYLIST, null=True,blank=True)
    location = models.CharField(max_length=200, choices=SITE)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_chosen = models.DateField(null=True)
    time_chosen = models.TimeField(null=True)
    services = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['name','phone']]

    def __str__(self):
        return '{}'.format(self.name)


class Worksite(models.Model):
    name = models.CharField(max_length=200)
    location = models.ForeignKey(Booking, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Employee(models.Model):
    site = models.ForeignKey(Site, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=200)

    def __str__(self):
        return self.name
