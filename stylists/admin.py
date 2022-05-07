from django.contrib import admin
from .models import Stylist

# Register your models here.


class StylistAdmin(admin.ModelAdmin):  
    list_display = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')


admin.site.register(Stylist, StylistAdmin)