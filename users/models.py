import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    SITE = (
        ('Papatoetoe', 'Papatoetoe'),
        ('Onehunga','Onehunga')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, choices=SITE, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to='photos/users/', default="profiles/user-default.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return str(self.user.username)
