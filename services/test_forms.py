from django.test import TestCase
from .forms import ServiceForm

# Create your tests here.

class TestServiceForm(TestCase):

    def test_service_name_is_required(self):
        form = ServiceForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_service_price_is_required(self):
        form = ServiceForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ServiceForm()
        self.assertEqual(form.Meta.fields, ['name', 'service_type', 'price'])

    # def test_can_capitalize_method(self):
    #     service = ServiceForm({'name': 'test delete service'})
    #     response = self.client.post(f'/services/edit/{service.id}', {'name': 'test edit check'})
    #     self.assertRedirects(response, '/services/')
    #     self.assertEqual(updated_item.name, 'Test edit check')


