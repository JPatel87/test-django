from django.shortcuts import render, redirect
from .import forms

# Create your views here.
def get_bookings_page(request):
    if request.method == 'POST':
        form = forms.CreateBooking(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('manage_booking')
    else:
        form = forms.CreateBooking()
    return render(request, 'bookings/create-booking.html', {'form':form})

def manage_bookings_page(request):
    return render(request, 'bookings/manage-booking.html')