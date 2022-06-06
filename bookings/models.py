from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Timeslot(models.Model):
    class Meta:
        unique_together = ('date', 'time', 'stylist')
    
    TIMESLOT_LIST = (
        (0, '6PM'),
        (1, '7PM'),
        (2, '8PM'),
        (3, '9PM')
    )

    def validate_date(self):
        if self < date.today():
            raise ValidationError("Date cannot be in the past")

    date = models.DateField(
        validators=[validate_date]
        )

    time = models.IntegerField(choices=TIMESLOT_LIST)
    stylist = models.ForeignKey('stylists.Stylist', on_delete=models.CASCADE, default=2)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, default=50)
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="timeslot", default=''
    )

    def __str__(self):
        return f'{self.date} - {self.get_time_display()} - {self.stylist}'

    @property
    def Is_Past(self):
        today = date.today()
        if self.date > today:
            return True
    

class Booking(models.Model):
    user = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="booking", default=''
    )
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')

    def validate_timeslot(self):
        if self < date.today():
            raise ValidationError("Date cannot be in the past")

    timeslot = models.OneToOneField(
        Timeslot,
        on_delete=models.CASCADE,
        default='',
        validators=[validate_timeslot]
        )
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.timeslot} - {self.service}'