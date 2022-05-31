from django.urls import path
from services.views import get_services_page, add_services_page


urlpatterns = [
    path('', get_services_page, name='services'),
    path('add/', add_services_page, name='add_services')
]