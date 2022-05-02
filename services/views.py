from django.shortcuts import render
from .models import Service

# Create your views here.
def get_services_page(request):
    cut_services = Service.objects.filter(service_type__contains = 'CUT').order_by('name')
    colour_services = Service.objects.filter(service_type__contains = 'COLOUR').order_by('name')
    style_services = Service.objects.filter(service_type__contains = 'STYLE').order_by('name')
    return render(request, 'services/services.html', {'cut_services': cut_services, 'colour_services': colour_services, 'style_services' : style_services})
