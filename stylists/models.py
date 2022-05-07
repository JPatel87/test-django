from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Stylist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    telephone = PhoneNumberField(default='')
    email = models.EmailField(max_length=254, default='')
    street_address_1 = models.CharField(max_length=50, default='')
    street_address_2 = models.CharField(max_length=50, null=True, blank=True)
    town_or_city = models.CharField(max_length=50, default='')
    postcode = models.CharField(max_length=10, default='')
    description = models.TextField(default='')
    image = CloudinaryField()

    def __str__(self):
        return self.first_name

    class Meta:
        unique_together = ('first_name', 'last_name')
