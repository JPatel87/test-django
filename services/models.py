from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Service(models.Model):
    class ServiceType(models.TextChoices):
        CUT = 'CUT', 'cut'
        COLOUR = 'COLOUR', 'colour'
        STYLE = 'STYLE', 'style'
    name = models.CharField(max_length=100, unique=True)
    service_type = models.CharField(
        max_length=10,
        choices=ServiceType.choices,
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('25.00')),
                    MaxValueValidator(Decimal('300.00'))],
        )

    def __str__(self):
        return self.name
