from django.db import models

# Create your models here.


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    stylist = models.ForeignKey('stylists.Stylist', on_delete=models.CASCADE, default=2)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, default=1)

