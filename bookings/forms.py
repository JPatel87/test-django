from django import forms
from .import models

class CreateBooking(forms.ModelForm):
    class Meta: 
        model = models.Appointment
        fields = ['first_name', 'last_name', 'service', 'appointment']