from django.urls import path
from bookings.views import get_bookings_page


urlpatterns = [
    path('', get_bookings_page, name='bookings')
]