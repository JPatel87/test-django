from django.urls import path
from services.views import get_services_page


urlpatterns = [
    path('', get_services_page, name='services')
]