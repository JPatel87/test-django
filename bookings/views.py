from django.shortcuts import render

# Create your views here.
def get_bookings_page(request):
    return render(request, 'bookings/bookings.html')