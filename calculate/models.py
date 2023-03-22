from django.db import models
from django.utils import timezone


# Create your models here.
class Record(models.Model):
    create_time = models.DateTimeField(default=timezone.now)
    data = models.JSONField(blank=True, null=True)
