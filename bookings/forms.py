from django import forms
from .models import Timeslot

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeslotFormAdmin(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['user', 'first_name', 'last_name', 'date', 'time', 'stylist', 'service']
        labels = {
            'first_name': 'Client First Name',
            'last_name': 'Client Last Name'
        }
        widgets = {
            'date': DateInput(),
        }

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['first_name', 'last_name', 'date', 'time', 'stylist', 'service']
        labels = {
            'first_name': 'Client First Name',
            'last_name': 'Client Last Name'
        }
        widgets = {
            'date': DateInput(),
        }