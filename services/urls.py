from django.urls import path
from services.views import get_services_page, add_services_page, edit_services_page, delete_services_page


urlpatterns = [
    path('', get_services_page, name='services'),
    path('add/', add_services_page, name='add_services'),
    path('edit/<service_id>', edit_services_page, name='edit_services'),
    path('delete/<service_id>', delete_services_page, name='delete_services')
]