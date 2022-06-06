from django.urls import path
from bookings.views import get_timeslot_page, get_bookings_page, edit_timeslot_page, delete_timeslot_page

urlpatterns = [
    path('', get_bookings_page, name='bookings'),
    path('create/timeslot/', get_timeslot_page, name='create_timeslot'),
    path('edit/<timeslot_id>', edit_timeslot_page, name='edit_timeslot'),
    path('delete/<timeslot_id>', delete_timeslot_page, name='delete_timeslot')
]
