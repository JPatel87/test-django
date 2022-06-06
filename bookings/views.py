from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Timeslot
from .forms import TimeslotForm

def get_bookings_page(request):
    user_filter = Timeslot.objects.filter(user__in=[request.user])
    timeslot = user_filter.order_by('date')
    context = {
        'timeslots': timeslot
    }
    return render(request, 'bookings/bookings.html', context)

def get_timeslot_page(request):
    if request.method == 'POST':
        form = TimeslotForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('bookings')
        else:
            return render(request, 'bookings/create_timeslot.html', context)
    form = TimeslotForm()
    context = {
        'form': form
    }

    return render(request, 'bookings/create_timeslot.html', context)


def edit_timeslot_page(request, timeslot_id):
    timeslot = get_object_or_404(Timeslot, id=timeslot_id)
    if request.method == "POST":
        form = TimeslotForm(request.POST, instance=timeslot)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('bookings')
        else:
            return render(request, 'bookings/edit_timeslot.html', context)
    form = TimeslotForm(instance=timeslot)
    context = {
        'form': form
    }
    return render(request, 'bookings/edit_timeslot.html', context)


def delete_timeslot_page(request, timeslot_id):
    timeslot = get_object_or_404(Timeslot, id=timeslot_id)
    if request.method == "POST":
        timeslot.delete()
        return redirect('bookings')
    context = {
        'timeslot': timeslot
    }
    return render(request, 'bookings/delete_timeslot.html', context)
