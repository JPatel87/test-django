from django.urls import path
from services.views import get_stylists_page


urlpatterns = [
    path('', get_stylists_page, name='stylists')
]