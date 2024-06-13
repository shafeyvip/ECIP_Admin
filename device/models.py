from django.db import models
from django.utils.text import slugify


# Create your models here.
DEVICE_TYPE = (
    ('PC','PC'),
    ('Laptop','Laptop'),
    ('Monitor','Monitor'),
    ('Printer','Printer'),
)

DEVICE_STATUS = (
    ('New','New'),
    ('Used','Used'),
    ('Damaged','Damaged'),
)
class device(models.Model):
    device_code = models.IntegerField(auto_created=True,default=7040000, unique=True)
    device_type = models.CharField(max_length=15, choices=DEVICE_TYPE)
    model_name = models.CharField(max_length=50)
    motherboard = models.CharField(max_length=50, null=True, blank=True)
    cpu = models.CharField(max_length=50, null=True, blank=True)
    ram = models.CharField(max_length=50, null=True, blank=True)
    hdd = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=DEVICE_STATUS)
    sites = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    other = models.TextField(max_length=255)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.device_code) ## logic
        super(device,self).save(*args, **kwargs)

    def __str__(self):
        return self.model_name

