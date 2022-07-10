from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

from bookings.models import Booking, Service

# Create your views here.
def createBooking(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'bookings/index.html', context)


def booking(request):

    

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        stylist_name = request.POST.get('stylist_name', False)
        location = request.POST.get('location', False)
        description = request.POST.get('description')
        date_chosen = request.POST.get('date_chosen', False)
        time_chosen = request.POST.get('time_chosen', False)
        services = request.POST.getlist('services[]'),            

        print(services)
    

        booking = Booking(
            name = name,
            email = email,
            phone = phone,
            location = location,
            stylist_name = stylist_name,
            description = description,
            date_chosen = date_chosen,
            time_chosen = time_chosen,
            services = services,

            )

        booking.save()
        messages.success(request, 'Booking Confirm! Thank you and see you')
        return redirect('index')