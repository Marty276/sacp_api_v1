from django.db import models
from datetime import date
# Create your models here.

class Requests(models.Model):
    address = models.CharField(max_length = 200)
    date = models.DateField(default = date.today)
    work_data = models.JSONField()
    worker_name = models.CharField(max_length = 200, blank = True)

    def __str__(self):
        return self.address

class To_Collect(models.Model):
    address = models.CharField(max_length = 200)
    date = models.DateField()
    work_data = models.JSONField()
    worker_name = models.CharField(max_length = 200, blank = True)
    total_amount = models.IntegerField(default = 0)
    send_to_collect = models.BooleanField(default = False)
    collect_date = models.DateField(blank = True)

class To_Pay_Or_Paid(models.Model):
    address = models.CharField(max_length = 200)
    date = models.DateField()
    work_data = models.JSONField()
    worker_name = models.CharField(max_length = 200, blank = True)
    total_amount = models.IntegerField(default = 0)
    paid_by_company = models.BooleanField(default = False)
    work_data_to_pay = models.JSONField()
    total_amount_to_pay = models.IntegerField(default = 0)
    paid = models.BooleanField(default = False)
    pay_date = models.DateField(blank = True)
    amount_earned = models.IntegerField(default = 0)

