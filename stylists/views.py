from django.shortcuts import render
from .models import Stylist

# Create your views here.
def get_stylists_page(request):
    stylist = Stylist.objects.all()
    return render(request, 'stylists/stylists.html', {'stylists':stylist})
