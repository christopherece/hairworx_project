from multiprocessing import context
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

from bookings.models import Booking, Employee, Service, Site

def get_stylists_ajax(request):
    if request.method == "POST":
        site_id = request.POST['site_id']
        try:
            site = Site.objects.filter(id = site_id).first()
            employees = Employee.objects.filter(site = site)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        
        return JsonResponse(list(employees.values('id', 'name')), safe = False) 


def createBooking(request):
    services = Service.objects.all()
    sites = Site.objects.all()
    context = {'services':services, 'sites':sites}
    return render(request, 'bookings/index.html', context)


def booking(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        stylist_name = request.POST.get('stylist_name', False)
        site = Site.objects.get(id=request.POST["site"])
        description = request.POST.get('description')
        date_chosen = request.POST.get('date_chosen', False)
        time_chosen = request.POST.get('time_chosen', False)
        services = request.POST.getlist('services[]'),                

        booking = Booking(
            name = name,
            email = email,
            phone = phone,
            site = site,
            stylist_name = stylist_name,
            description = description,
            date_chosen = date_chosen,
            time_chosen = time_chosen,
            services = services,

            )

        booking.save()
        messages.success(request, 'Booking Confirm! Thank you and see you')
        return redirect('index')