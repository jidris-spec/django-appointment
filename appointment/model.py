from django.db import models

class Appointment(models.Model):
    service = models.CharField(max_length=100)
    # other fields
