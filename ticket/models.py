from django.db import models
from employee.models import employee

from django.utils.text import slugify

# Create your models here.

class IT(models.Model):
    it_name = models.CharField(max_length=25)
    it_id = models.IntegerField(unique=True)
    def __str__(self):
        return self.it_name

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    ticket_code = models.IntegerField(auto_created=True, default=1000, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    requested_by = models.ForeignKey(employee, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(IT, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_RESOLVED = 'resolved'
    STATUS_CLOSED = 'closed'

    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_RESOLVED, 'Resolved'),
        (STATUS_CLOSED, 'Closed'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
    )
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.ticket_code)  ## logic
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class New_Ticket(models.Model):
        pass

