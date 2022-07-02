from distutils.command.upload import upload
import uuid
from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/gallery')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name