from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    second_address = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    customer_name = models.CharField(max_length=200, default=None)
    date = models.CharField(max_length=200, default=None)
    service = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.service} on {self.date} for {self.customer_name}"
