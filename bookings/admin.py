from django.contrib import admin
from .models import Appointment, TimeSlot

# Register your models here.

@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'stylist')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):  
    list_display = ('first_name', 'last_name', 'service', 'appointment')
