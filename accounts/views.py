from django.shortcuts import redirect, render

from bookings.models import Booking

# Create your views here.
def login(request):
    return render (request, 'accounts/login.html')

def register(request):
    return render (request, 'accounts/register.html')

def logout(request):
    return redirect ('index')

def dashboard(request):
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'accounts/dashboard.html', context)
