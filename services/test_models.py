from django.test import TestCase
from .models import Service

# Create your tests here.

class TestModels(TestCase):
    
    def test_item_string_method_returns_name(self):
        service = Service.objects.create(name='Test Todo Item', service_type='cut', price='10')
        self.assertEqual(str(service), 'Test Todo Item')
