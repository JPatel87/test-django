from django.contrib import admin
from .models import Timeslot, Booking

# Register your models here.

@admin.register(Timeslot)
class TimeslotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'stylist', 'first_name', 'last_name', 'service')
    # readonly_fields =('user',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):  
    list_display = ('first_name', 'last_name', 'service', 'timeslot')
