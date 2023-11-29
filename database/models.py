from django.db import models
from datetime import date
# Create your models here.

class Works(models.Model):
    address = models.CharField(max_length=256, blank=False)
    work_data = models.JSONField(blank=False)
    worker_name = models.CharField(max_length=256, blank=False)
    company_name = models.CharField(max_length=256, blank=True)
    totals = models.JSONField(blank=True)
    status = models.CharField(max_length=256, blank=False)
    dates = models.JSONField(blank=False)
    notes = models.TextField(max_length=1024, blank=True)