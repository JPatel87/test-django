from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# Create your models here.


class Stylist(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    telephone = PhoneNumberField(default='')
    years_experience = models.PositiveIntegerField(default=1)
    background_details = models.CharField(max_length=250, default='')
    image = CloudinaryField('image', default='')

    def __str__(self):
        return self.first_name
