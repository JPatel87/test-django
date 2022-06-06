from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta: 
        model = Service
        fields = ['name', 'service_type', 'price']

    def clean_title(self):
        return self.cleaned_data['name'].capitalize()