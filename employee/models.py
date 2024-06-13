from django.db import models
from django.utils.text import slugify

# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "employee/%s.%s"%(instance.employee_code,extension)

class employee(models.Model):
    employee_code = models.IntegerField(auto_created=True, default=1000, unique=True)
    employee_name = models.CharField(max_length=50)
    employee_national_id = models.IntegerField()
    birth_date = models.DateField(max_length=8)
    employee_phone_1 = models.IntegerField()
    employee_phone_2 = models.IntegerField(null=True, blank=True)
    governorate = models.CharField(max_length=25)
    employee_email = models.CharField(max_length=50)
    image = models.ImageField(upload_to=image_upload, null=True, blank=True)

    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.employee_code)  ## logic
        super(employee, self).save(*args, **kwargs)

    def __str__(self):
        return self.employee_name

