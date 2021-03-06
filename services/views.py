from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service
from .forms import ServiceForm

# Create your views here.
def get_services_page(request):
    cut_services = Service.objects.filter(service_type__contains='CUT').order_by('name')
    colour_services = Service.objects.filter(service_type__contains='COLOUR').order_by('name')
    style_services = Service.objects.filter(service_type__contains='STYLE').order_by('name')
    return render(request, 'services/services.html', {'cut_services': cut_services, 'colour_services': colour_services, 'style_services' : style_services})

def add_services_page(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request was successfully made', extra_tags='success_services')
            return redirect('services')
        else:
            messages.error(request, 'Service not added - please address errors', extra_tags='invalid_add_services')
            return render(request, 'services/add_services.html', context)
    form = ServiceForm()
    context = {
        'form': form
    }
    return render(request, 'services/add_services.html', context)

def edit_services_page(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request was successfully made', extra_tags='success_services')
            return redirect('services')
        else:
            messages.error(request, 'Service not edited - please address errors', extra_tags='invalid_edit_services')
            return render(request, 'services/edit_services.html', context)
    form = ServiceForm(instance=service)
    context = {
        'form': form
    }
    return render(request, 'services/edit_services.html', context)

def delete_services_page(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        service.delete()
        messages.success(request, 'Your request was successfully made', extra_tags='success_services')
        return redirect('services')
    context = {
        'service': service
    }
    return render(request, 'services/delete_services.html', context)


