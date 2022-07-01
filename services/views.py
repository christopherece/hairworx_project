from multiprocessing import context
from django.shortcuts import render

from services.models import Service

# Create your views here.
def index(request):
    services = Service.objects.all()
    context = {'services': services }
    return render(request, 'services/services.html', context)

def service(request, pk):
    return render(request, 'services/service.html')