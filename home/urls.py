from django.urls import path
from home.views import get_home_page


urlpatterns = [
    path('', get_home_page, name='home')
]