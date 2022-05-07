from django.shortcuts import render

# Create your views here.
def get_stylists_page(request):
    return render(request, 'stylists/stylists.html')
