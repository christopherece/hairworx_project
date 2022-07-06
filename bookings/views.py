from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

from bookings.models import Booking

# Create your views here.
def createBooking(request):
    return render(request, 'bookings/index.html')


def booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        location = request.POST.get('location', False)
        description = request.POST['description']
        date_chosen = request.POST.get('date_chosen', False)
        time_chosen = request.POST.get('time_chosen', False)

        booking = Booking(
            name = name,
            email = email,
            phone = phone,
            location = location,
            description = description,
            date_chosen = date_chosen,
            time_chosen = time_chosen
        )

        booking.save()
        messages.success(request, 'Booking Confirm! Thank you and see you')
        return redirect('index')