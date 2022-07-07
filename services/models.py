from distutils.command.upload import upload
import uuid
from django.db import models

# Create your models here.
class Service(models.Model):
    SERVICE_TYPE = (
        ('startprice','Starting Price'),
        ('colourservice', 'Colour Services'),
        ('lighteningservice', 'Lightening Services'),
        ('kerat','Keratin Straight Permanent'),
        ('treatment','Treatment'),
        ('styling', 'Styling'),
        ('extension', 'Extension')
    )
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='photos/services')
    service_type = models.CharField(max_length=200, choices=SERVICE_TYPE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name