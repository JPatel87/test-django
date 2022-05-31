from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TimeSlot(models.Model):
    date = models.DateField()
    time = models.CharField(max_length=5, default='')
    stylist = models.ForeignKey('stylists.Stylist', on_delete=models.CASCADE, default=2)

    def __str__(self):
        return f'{self.date} {self.time} - {self.stylist}'


class Appointment(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="appointment", default=''
    )
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    appointment = models.OneToOneField(TimeSlot, on_delete=models.CASCADE, default='')
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, default=1)
