from django import forms
from .models import Timeslot

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeslotForm(forms.ModelForm):
    class Meta:
        model = Timeslot
        fields = ['first_name', 'last_name', 'date', 'time', 'stylist', 'service']
        widgets = {
            'date': DateInput(),
        }

    # def clean_first_name(self):
    #     return self.cleaned_data['first_name', 'last_name'].capitalize()
    