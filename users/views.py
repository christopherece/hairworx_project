from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from bookings.models import Booking
from django.contrib.auth.decorators import login_required


# Create your views here.
def loginPage(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

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
            return redirect('dashboard')

    return render (request, 'users/login.html')

def register(request):
    return render (request, 'accounts/register.html')

def logoutUser(request):
    logout(request)
    return redirect ('login')

@login_required(login_url='login')
def dashboard(request):
    bookings = Booking.objects.all()
    context = {'bookings':bookings}
    return render(request, 'users/dashboard.html', context)

def profiles(request):
    return redirect ('index')
