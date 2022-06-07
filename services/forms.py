from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    class Meta: 
        model = Service
        fields = ['name', 'service_type', 'price']
        labels = {
            'name': 'Service name',
            'price': 'Price (£)',
        }
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'e.g £50, enter as 50'}),
        }

    def clean_name(self):
        return self.cleaned_data['name'].capitalize()
