from django.urls import path
from bookings.views import get_bookings_page, manage_bookings_page

urlpatterns = [
    path('create/', get_bookings_page, name='create_booking'),
    path('manage/', manage_bookings_page, name='manage_booking')
]