from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# Create your models here.


class Stylist(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    telephone = PhoneNumberField(default='')
    email = models.EmailField(max_length=254, default='')
    background = models.TextField(default='')
    image = CloudinaryField('image', default='')

    def __str__(self):
        return self.first_name
