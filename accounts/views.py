from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from bookings.models import Booking

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try: 
            user = User.objects.get(username=username)
        except:
            print('Username does not exist!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

    return render (request, 'accounts/login.html')

def register(request):
    return render (request, 'accounts/register.html')

def logout(request):
    return redirect ('index')

def dashboard(request):
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'accounts/dashboard.html', context)
