from django.db import models

# Create your models here.


class Worker(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    fname = models.CharField(max_length=50)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=20)
    worker_tip = models.CharField(max_length=20)
    today_money = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.fname


class User(models.Model):
    id = models.CharField(max_length=30, primary_key=True)
    fname = models.CharField(max_length=100, null=True, blank=True)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    comment = models.CharField(max_length=500, null=True, blank=True)
    total_order = models.CharField(max_length=20, null=True, blank=True)
    time_order = models.CharField(max_length=100, null=True, blank=True)
    time_started = models.CharField(max_length=100, null=True, blank=True)
    time_finished = models.CharField(max_length=100, null=True, blank=True)
    packer = models.CharField(max_length=20, null=True, blank=True)
    curier = models.CharField(max_length=20, null=True, blank=True)
    accepted_prinse = models.CharField(max_length=20, null=True, blank=True)
    worker_id = models.ForeignKey(
        'Worker', on_delete=models.CASCADE, related_name='user_for_worker')

    def __str__(self):
        return self.fname


class WorkerReport(models.Model):
    date = models.CharField(max_length=50)
    prince = models.CharField(max_length=20)
    worker_id = models.ForeignKey(
        'Worker', on_delete=models.CASCADE, related_name='report_worker')

    def __str__(self):
        return self.date


class OrderForUser(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    img_link = models.CharField(max_length=500, null=True, blank=True)
    size = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.CharField(max_length=100, null=True, blank=True)
    user_id = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='order_for_user')

    def __str__(self):
        return self.name
