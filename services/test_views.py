from django.test import TestCase
from .models import Service

# Create your tests here.

class TestViews(TestCase):

    def test_get_services(self):
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/services.html')

    def test_get_add_services_page(self):
        response = self.client.get('/services/add/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/add_services.html')


    def test_get_edit_services_page(self):  
        service = Service.objects.create(name='Test edited service', service_type='cut', price='10')
        response = self.client.get(f'/services/edit/{service.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/edit_services.html')
        

    def test_can_add_service(self):
        response = self.client.post('/services/add/', {'name': 'Test added service', 'service_type':'cut', 'price':'10'})
        self.assertRedirects(response, '/services/add')


    def test_can_delete_item(self):
        service = Service.objects.create(name='Test delete service', service_type='cut', price='10')
        response = self.client.get(f'/services/delete/{service.id}')
        self.assertRedirects(response, '/services')
        existing_items = Service.objects.filter(id=service.id)
        self.assertEqual(len(existing_items), 0)


    def test_can_edit_service(self):
        service = Service.objects.create(name='Test delete service', service_type='cut', price='10')
        response = self.client.post(f'/services/edit/{service.id}', {'name': 'Test edit check'})
        self.assertRedirects(response, '/services/')
        updated_item = Service.objects.get(id=service.id)
        self.assertEqual(updated_item.name, 'Test edit check')
